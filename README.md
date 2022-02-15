# Enrich_Omics: A Python wrapper for EnrichR and OpenTargets
 [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
 [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
 [![GitHub Issues](https://img.shields.io/github/issues/saramasarone/enrich_omics.svg)](https://github.com/saramasarone/enrich_omics/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/saramasarone/enrich_omics.svg)](https://github.com/saramasarone/enrich_omics/pulls)



## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Tutorial](#tutorial)
- [Docs](#docs)

## About <a name = "about"></a>
Python wrapper for EnrichR and OpenTargets API. Allows for visualisation of enriched pathways or disease associated to a given target

#### EnrichR
- Choose from all EnrichR libraries (Transcription, Pathways, Drugs, etc). Default library is KEGG_pathways_2021
- Get table with enrichment results
- Plot with enrichment results ans export it

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

## Installation <a name = "installation"></a>
```python

pip install enrich-omics

```

## Tutorial <a name="tutorial"></a>
### EnrichR API
``` python
import enrich_omics
from enrich_omics import EnrichR
from enrich_omics import OpenTargets

# get all available libraries
EnrichR.get_libraries()

# get enrichment for a list of genes/proteins
# default library is 'KEGG_2021_Human' but other libraries can be specified using the 'library_name' argument.
# check out available libraries with the command above

gene_list = ['LMNA', 'MYH7', 'TNNT2', 'ACE2']
EnrichR.plot_enrichment(gene_list, library_name='KEGG_2021_Human', height = 300, width = 600, max_hits = None)
```
![image](https://raw.githubusercontent.com/saramasarone/enrich_omics/main/Pictures/Plot_enrichment.png)

```python
# specifying a different library
EnrichR.plot_enrichment(gene_list, library_name = 'BioPlanet_2019', height = 200, width = 300, max_hits= None)
```
![image](https://raw.githubusercontent.com/saramasarone/enrich_omics/main/Pictures/Plot_enrichment2.png)
```python
# get results as table for downstream analysis/ pipeline integration
EnrichR.get_table_enrichment(['LMNA', 'MYH7', 'TNNT2', 'ACE2'], library_name='KEGG_2021_Human')
```
![image](https://raw.githubusercontent.com/saramasarone/enrich_omics/main/Pictures/Get_table_enrichment.png)

### Open Targets API (Open Targets currently only supports single target enrichment. More information on the OpenTargets website)
```python
# OpenTargets takes EnsembleIDs by default, but entrez ids can be passed using the argument entrez = True
# Export plots easily in png or svg
OpenTargets.plot_diseases(target_id = 'PLG', entrez = True) 
```
![image](https://raw.githubusercontent.com/saramasarone/enrich_omics/main/Pictures/Plot_diseases.png)

```python
OpenTargets.get_table_drugs(target_id = 'PLG', entrez = True)
```
![image](https://raw.githubusercontent.com/saramasarone/enrich_omics/main/Pictures/Get_table_drugs.png)

```python
# Plot drugs and diseases associated to a given target
OpenTargets.plot_drugs_disease(target_id = 'PLG', entrez = True)
```
![image](https://raw.githubusercontent.com/saramasarone/enrich_omics/main/Pictures/PLot_drug_disease.png)

## Docs <a name = "docs"></a>
Documentation for this package can be found [here](https://enrich-omics.readthedocs.io/en/latest/opentargets.html)

Contributions always welcome!


