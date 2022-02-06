# enrich_omics
 [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
 [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)


## 📝 Table of Contents
- [About](#about)
- [Installation](#installation)
- [Tutorial](#tutorial)
- [Contributing](#contributing)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)


## About <a name = "about"></a>
Python wrapper for EnrichR and OpenTargets API. Allows for visualisation of pathways enriched and disease associated to a given target or disease

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
 Tutorials coming soon

## Contributiong <a name = "contributing"></a> 
  
## Authors <a name = "authors"></a>
- [@saramasarone](https://github.com/saramasarone) 

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- Hat tip to anyone whose code was used
- Inspiration
- References
