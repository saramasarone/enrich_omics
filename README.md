# ApplePy
Python wrapper for EnrichR and OpenTargets API. Allows for visualisation of pathways enriched and disease associated to a given target or disease

## EnrichR
- Choose from all EnrichR libraries (Transcription, Pathways, Drugs, etc). Default library is "KEGG_pathways_2021"
- Get table with enrichment results
- Get plot with enrichment results

## OpenTargets
Open Target is currently only supporting the search of a single target
- Convert Entrz to Ensemble if needed (OpenTargets API accepts only Ensemble IDs)
- Get decsritpion of the function of the target
- Get diseases associated to a certain target
- Plot diseases associated to a certain target
- Get table drugs associated to a certain target
- Plot the drugs that work for a given target and the diseases associated to it
- Plot the drugs associated to a given target and the trial phase they are currently in
