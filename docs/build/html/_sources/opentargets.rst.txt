OpenTargets API
===============
The OpenTargets API allows to extract information about drugs and diseases associated to a single target (either a gene or a disease). Currently OpenTargets only supports single queries.

.. code:: python

	# OpenTargets takes EnsembleIDs by default, but entrez ids can be passed 		using the argument entrez = True
	# Export plots easily in png or svg
	OpenTargets.plot_diseases(target_id = 'PLG', entrez = True) 

Users can get a table with the drugs associated to a particular target and use it for downstream analysis or they can directly plot the results 

.. code:: python

	OpenTargets.get_table_drugs(target_id = 'PLG', entrez = True)
	# Plot drugs and diseases associated to a given target
	OpenTargets.plot_drugs_disease(target_id = 'PLG', entrez = True)
