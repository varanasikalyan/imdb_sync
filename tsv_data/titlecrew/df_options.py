from collections import OrderedDict

df_options = OrderedDict()

df_options['titledirectors'] = {
		'index': 'tconst',
		'columns': ['tconst', 'directors'],
		'dtype': {'tconst':'object', 'directors':'object'},
		'mapping': {'\\N': None},				
		'un_group_by': {'tconst': 'directors'}
	}

df_options['titlewriters'] = {
		'index': 'tconst',
		'columns': ['tconst', 'writers'],
		'dtype': {'tconst':'object', 'writers':'object'},
		'mapping': {'\\N': None},
		'un_group_by': {'tconst': 'writers'}
	}