Introduction
===============

Welcome to enrich_omics package!!
enrich-omics is a package that allows to perform enrichment analysis directly from python without the need to use a webapp or external tool (that often require copy-pasting lists of genes).

Through enrich-omics you can use both the EnrichR and OpenTargets APIs directly to get enrichment results as well as pathways, processeses, terms and drugs associated to a given target or set of targets.

* EnrichR
- Choose from all EnrichR libraries (Transcription, Pathways, Drugs, etc). Default library is KEGG_pathways_2021
- Get table with enrichment results
- Plot with enrichment results ans export it

* OpenTargets
Open Target is currently only supporting the search of a single target

#### Target endpoint
- Convert Entrez to Ensemble if needed (OpenTargets API accepts only Ensemble IDs)
- Get description of the function of the target
- Get diseases associated to a certain target
- Plot diseases associated to a certain target
- Get table drugs associated to a certain target
- Plot the drugs that work for a given target and the diseases associated to it
- Plot the drugs associated to a given target and the trial phase they are currently in

*  Plots
- Export plots in SVG and PNG


*  Drug endpoint
- Get drug description
- Get a table with drug information (year of approval, drug type, toxicity, warnings)

