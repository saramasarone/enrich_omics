EnrichR
============
EnrichR API allows to extract information about pathways, transcription and drugs associated to a list of genesnor to a single gene.


.. code:: python

	import enrich_omics
	from enrich_omics import EnrichR
	from enrich_omics import OpenTarget

	# get all available libraries
	EnrichR.get_libraries()

	# get enrichment for a list of genes/proteins
	# default library is 'KEGG_2021_Human' but other libraries can be 	   specified using the 'library_name' argument.
	# check out available libraries with the command above

	gene_list = ['LMNA', 'MYH7', 'TNNT2', 'ACE2']
	EnrichR.plot_enrichment(gene_list)
