# Enrich_Omics: A Python wrapper for EnrichR and Open Targets
 [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
 [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)


## 📝 Table of Contents
- [About](#about)
- [Installation](#installation)
- [Tutorial](#tutorial)
- [Contributing](#contributing)

## About <a name = "about"></a>
Python wrapper for EnrichR and OpenTargets API. Allows for visualisation of enriched pathways or disease associated to a given target

#### EnrichR
- Choose from all EnrichR libraries (Transcription, Pathways, Drugs, etc). Default library is "KEGG_pathways_2021"
- Get table with enrichment results
- Get plot with enrichment results ans export it

#### OpenTargets
Open Target is currently only supporting the search of a single target

#### Target endpoint
- Convert Entrez to Ensemble if needed (OpenTargets API accepts only Ensemble IDs)
- Get description of the function of the target
- Get diseases associated to a certain target
- Plot diseases associated to a certain target
- Get table drugs associated to a certain target
- Plot the drugs that work for a given target and the diseases associated to it
- Plot the drugs associated to a given target and the trial phase they are currently in

#### Plots
- Export plots in SVG and PNG


#### Drug endpoint
- Get drug description
- Get a table with drug information (year of approval, drug type, toxicity, warnings)


## Installation <a name = "installation"></a>
```python

pip install enrich-omics

```

## Tutorial <a name="tutorial"></a>
### EnrichR API
``` python
import enrich_omics
from enrich_omics import EnrichR
from enrich_omics import OpenTarget

# get all available libraries
EnrichR.get_libraries()
```

```python
# get enrichment for a list of genes/proteins
# default library is 'KEGG_2021_Human' but specific libraries can be specified using the 'library_name' argument

gene_list = ['LMNA', 'MYH7', 'TNNT2', 'ACE2']
EnrichR.plot_enrichment(gene_list)

EnrichR.plot_enrichment(gene_list, library_name = 'BioPlanet_2019')
```
![image](https://github.com/saramasarone/enrich_omics/Pictures/plot_enrichment.png)
![image](https://github.com/saramasarone/enrich_omics/Pictures/plot_enrichment2.png)
```python
# get results as table for downstream analysis/ pipeline integration
EnrichR.get_table_enrichment(['LMNA', 'MYH7', 'TNNT2', 'ACE2'])
![image](https://github.com/saramasarone/enrich_omics/Pictures/Get_table_enrichment.png?raw=true)
```
### Open Targets API (Open Targets currently only supports single target enrichment. More information on the OpenTargets website)
```python
# OpenTargets takes EnsembleIDs by default, but entrez ids can be passed using the argument entrez = True
OpenTarget.plot_diseases(target_id = 'PLG', entrez = True) 
```
![image](https://github.com/saramasarone/enrich_omics/Pictures/plot_disease.png)

```python
OpenTarget.get_table_drugs(target_id = 'PLG', entrez = True)
```
![image](https://github.com/saramasarone/enrich_omics/Pictures/Get_table_drugs.png)

```python
# Plot drugs and diseases associated to a given target
OpenTarget.plot_drugs_disease(target_id = 'PLG', entrez = True)
```
![image](https://github.com/saramasarone/enrich_omics/Pictures/PLot_drug_disease.png)






