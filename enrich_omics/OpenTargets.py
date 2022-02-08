import json
import requests
import numpy as np
import altair as alt
import pandas as pd
import mygene


class OpenTargets(object):
    def __init__(self, gene_id):
        self.gene_id = gene_id
    
    @classmethod
    def entrez_to_ensembl(self, entrez):
        mg = mygene.MyGeneInfo()
        esbl = mg.query(entrez, fields='ensembl.gene')['hits'][0]['ensembl']['gene']
        return esbl
        
    @classmethod
    def function_description(self, gene_id):
        """ Get description of the function
        of the target """

        gene_id = gene_id
        query_string = """
        query target($ensemblId: String!){
            target(ensemblId: $ensemblId){
                id
                approvedSymbol
                alternativeGenes
                biotype
                functionDescriptions
        }
      }
            """
        variables = {"ensemblId": gene_id}
        base_url = "https://api.platform.opentargets.org/api/v4/graphql"
        r = requests.post(base_url, json={"query": query_string, "variables": variables})
        assert r.status_code == 200, 'Status code not 200'
        api_response_as_json = json.loads(r.text)
        return api_response_as_json

    @classmethod
    def get_associated_diseases(self, target_id, entrez = False): 
        target_id = target_id
        query_string = """
          query target($ensemblId: String!){
            target(ensemblId: $ensemblId){
              approvedSymbol
              id
              associatedDiseases{
                count
                rows{
                    disease{
                        id
                        name
                    }
                    score
                    datasourceScores{
                      id
                      score
                    }
                   }
              }
            }
          }
        """
        if entrez == True:
            target_id = self.entrez_to_ensembl(target_id)
            
        # Set variables object of arguments to be passed to endpoint
        variables = {"ensemblId": target_id}
        base_url = "https://api.platform.opentargets.org/api/v4/graphql"
        r = requests.post(base_url, json={"query": query_string, "variables": variables})
        assert r.status_code == 200, 'Status code not 200'
        api_response_as_json = json.loads(r.text)

        return api_response_as_json

    @classmethod
    def plot_diseases(self, target_id, max_hit = None, height= 300, width = 300, entrez=False):
        
        if entrez == True:
            target_id = self.entrez_to_ensembl(target_id)
            print(target_id)
        
        response = self.get_associated_diseases(target_id)
        dis_labels =[]
        score=[]
        for i in response['data']['target']['associatedDiseases']['rows']:
            dis_labels.append(i['disease']['name'])
            score.append(i['score'])

        df = pd.DataFrame(score, columns = ['score'])
        df['labels'] = dis_labels
        df['score'] = np.round(score, 3)
        if max_hit == None:
            max_hit = len(df)
        df = df.iloc[0:max_hit, :]
        bars = alt.Chart(df).mark_bar().encode(
        x='score', y = alt.Y('labels', sort= '-x'))
        text = bars.mark_text(
        align='left',
        baseline='middle',
        dx=4
        ).encode(text='score:Q').properties(title='Diseases associated to the target - '+ str(target_id))

        return (bars+text).properties(height=height, width = width)

    @classmethod
    def get_drugs(self, target_id, entrez = False):

        query_string = """
        query target($ensemblId: String!){
        target(ensemblId: $ensemblId){
            id
            approvedSymbol
            approvedName
            biotype
            geneticConstraint {
              constraintType
              exp
              obs
              score
              oe
              oeLower
              oeUpper
            }
            knownDrugs {
              uniqueDrugs
          uniqueTargets
          count
          cursor
          rows{
            approvedName
            prefName
            drugType
            phase
            mechanismOfAction
            disease{
            name
            }
          }
        }

      }
    }
    """    
        if entrez == True:
            target_id = self.entrez_to_ensembl(target_id)
 
        variables = {"ensemblId": target_id}
        base_url = "https://api.platform.opentargets.org/api/v4/graphql"
        r = requests.post(base_url, json={"query": query_string, 
                                          "variables": variables})
        api_response_as_json = json.loads(r.text)

        return api_response_as_json

    @classmethod
    def get_table_drugs(self, target_id, entrez = False):
        drug_name=[]
        mech_act =[]
        drugtype=[]
        approvedname=[]
        dis_name=[]
        phase=[]
        
        if entrez == True:
            target_id = self.entrez_to_ensembl(target_id)
 
        res = self.get_drugs(target_id)
        if res['data']['target']['knownDrugs'] is None:
            return "No drug data available"

        for i in res['data']['target']['knownDrugs']['rows']:
            drug_name.append(i['prefName'])
            mech_act.append(i['mechanismOfAction'])
            drugtype.append(i['drugType'])
            approvedname.append(i['approvedName'])
            dis_name.append(list(i['disease'].values()))
            phase.append(i['phase'])

        drug_table = pd.DataFrame(drug_name, columns =['drugName']) 
        drug_table['mechanismOfAction'] = mech_act
        drug_table['drugType'] = drugtype
        drug_table['approvedName'] = approvedname
        drug_table['diseaseName'] = dis_name
        drug_table['trialPhase'] = phase
        drug_table['trialPhase'].replace({1:"I", 2:"II", 3:"III", 4: "IV", 5:"V"}, inplace=True)

        dis =[]
        for i in drug_table['diseaseName']:
            for terms in i:
                   dis.append(terms)
        drug_table = drug_table.drop(columns=["diseaseName"])
        drug_table['diseaseName'] = dis
        return drug_table

    @classmethod
    def plot_drugs_disease(self, target_id, max_hits = None, entrez = False):

        """ returns the plot of
        drugs that work for that target
        and the diseases associated to it
        """
        if entrez == True:
            target_id = self.entrez_to_ensembl(target_id)
        table = self.get_table_drugs(target_id)
        if isinstance(table, str):
            return "No data available"
        else:
            if max_hits == None:
                max_hits = len(table)
            plot = alt.Chart(table.iloc[0:max_hits,]).mark_bar().encode(
            x='drugName',
            y='diseaseName',
            color='mechanismOfAction'
            ).properties(title="Known Drugs - " + str(target_id))
            return plot

    @classmethod
    def plot_drugs_phase(self, target_id, max_hits = None, entrez = False):

        """ returns the plot of
        drugs and the phase they 
        are involved in"""
        
        if entrez == True:
            target_id = self.entrez_to_ensembl(target_id)
        
        table = self.get_table_drugs(target_id)
        
        if isinstance(table, str):
            return "No data available"
        else:
            if max_hits == None:
                max_hits = len(table)
            plot = alt.Chart(table.iloc[0:max_hits,]).mark_bar().encode(
            x='drugName',
            y='count(drugName)',
            color='trialPhase').properties(title="Trial Phase - " + str(target_id))
            return plot


