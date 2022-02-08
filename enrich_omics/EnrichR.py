import json
import requests
import numpy as np
import altair as alt
import pandas as pd
import mygene



class EnrichR(object):
    def __init__(self, list_genes):
        self.list_genes = list_genes
        self.len_list = len(list_genes)
    
    @classmethod
    def get_libraries(self):
        """return active enrichr library name. Official API """

        lib_url='https://maayanlab.cloud/Enrichr/datasetStatistics'
        response = requests.get(lib_url, verify=True)
        if not response.ok:
            raise Exception("Error getting the Enrichr libraries")
        libs_json = json.loads(response.text)
        libs = [lib['libraryName'] for lib in libs_json['statistics']]

        return sorted(libs)
    
    @classmethod
    def get_id(self, list_genes):
        ENRICHR_URL = 'https://maayanlab.cloud/Enrichr/addList'
        genes_str = '\n'.join(list_genes)
        description = 'Example gene list'
        payload = {
        'list': (None, genes_str),
        'description': (None, description)
        }

        response = requests.post(ENRICHR_URL, files=payload)
        if not response.ok:
            raise Exception('Error analyzing gene list')
        data = json.loads(response.text)
        user_id = data['userListId']
        return user_id
    
    @classmethod
    def get_enrichment(self, list_genes, library_name='KEGG_2021_Human'):
        '''Rank, Term name, P-value, Z-score, Combined score, 
        Overlapping genes, Adjusted p-value, Old p-value, 
        Old adjusted p-value. Dafault library is Kegg 2021'''
        
        user_id = self.get_id(list_genes)
        ENRICHR_URL = 'https://maayanlab.cloud/Enrichr/enrich'
        query_string = '?userListId=%s&backgroundType=%s'
        user_list_id = user_id
        gene_set_library = library_name
        response = requests.get(
        ENRICHR_URL + query_string % (user_list_id, gene_set_library))

        if not response.ok:
            raise Exception('Error fetching enrichment results')

        res = json.loads(response.text)
        return res, gene_set_library
    
    @classmethod
    def get_table_enrichment(self, list_genes, library_name='KEGG_2021_Human'):
        dct = self.get_enrichment(list_genes)
        df = pd.DataFrame(dct[0][library_name])
        df.columns = ['Rank', 'Term name', 'P-value', 'Z-score', 'Combined score', 
        'Overlapping genes', 'Adjusted p-value', 'Old p-value', 
        'Old adjusted p-value']
        return df
    
    
    @classmethod
    def plot_enrichment(self, list_genes, library_name='KEGG_2021_Human', height = 200, width = 300, max_hits = None):
        '''Plot ordered enrichment scores 
        as -log10(pval)'''

        if library_name=='KEGG_2021_Human':
            library_name = self.get_enrichment(list_genes)[1]
            res = self.get_enrichment(list_genes)[0]
        else:
            library_name = library_name
            res = self.get_enrichment(list_genes, library_name = library_name)[0]
        labels=[]
        p_val=[]
        for i in range(0, len(res[library_name])):
            labels.append(res[library_name][i][1])
            p_val.append(res[library_name][i][2]) 
        df_plot= pd.DataFrame(labels,columns=['labels'])
        df_plot['pval'] = p_val
        df_plot['-log(pval)'] = np.round(-np.log(df_plot['pval']),2)
        
        if max_hits == None:
            max_hits = len(df_plot)
        
        df_plot = df_plot.iloc[0:max_hits,:]    
        bars = alt.Chart(df_plot).mark_bar(color = 'indianred').encode(
            x='-log(pval)', y = alt.Y('labels', sort= '-x'))
        text = bars.mark_text(
            align='left',
            baseline='middle',
            dx=4 
        ).encode(text='-log(pval):Q').properties(title='Enrichment results - '+str(library_name))

        return (bars+text).properties(height=height, width = width)
        

