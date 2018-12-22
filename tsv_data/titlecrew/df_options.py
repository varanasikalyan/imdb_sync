from collections import OrderedDict

df_options = OrderedDict()

df_options['titledirectors'] = {
		'columns': ['tconst', 'directors'],
		'dtype': {'tconst':'object', 'directors':'object'},
		'mapping': {'\\N': None}
	}

df_options['titlewriters'] = {
		'columns': ['tconst', 'writers'],
		'dtype': {'tconst':'object', 'writers':'object'},
		'mapping': {'\\N': None}
	}