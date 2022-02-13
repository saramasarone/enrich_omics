.. enrich_omics documentation master file, created by
   sphinx-quickstart on Sat Feb 12 20:05:49 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to **enrich_omics** package!
=====================================================

Enrich_omics is a package that allows users to perform enrichment analysis directly from Python without the need to use webapps or external tools (that often require copy-pasting lists of genes and can thus be error-prone).

Through enrich_omics you can use both the EnrichR and OpenTargets APIs to get enrichment results, as well as pathways, processeses, terms and drugs associated to a given target or set of targets. Targets can either be genes or proteins.

EnrichR API
------------

* Choose from all EnrichR libraries (Transcription, Pathways, Drugs, etc). 
* Default library is **KEGG pathways 2021**
* Get table with enrichment results
* Plot with enrichment results ans export it


Open Targets API
-----------------

`Open Targets <hhttps://www.opentargets.org/>`_ uses human genetics and genomics data for systematic drug target identification and prioritisation. 
Open Target is currently only supporting single targets searches.

Target endpoint
***************

* Convert Entrez ID to Ensemble ID if needed (OpenTargets API only accepts Ensemble IDs)
* Get description of the biological function of the target
* Get diseases associated to a certain target
* Plot diseases associated to a certain target
* Get table drugs associated to a certain target
* Plot the drugs that work for a given target and the diseases associated to it
* Plot the drugs associated to a given target and the trial phase they are     currently in


Exporting plots for reports and publications
*********************************************

* Export plots in SVG and PNG


Source code
***************

The source code can be found at https://github.com/saramasarone/enrich_omics



Index
-------

.. Hidden TOCs

.. toctree::
   
   installing
   enrichr
   opentargets
	


