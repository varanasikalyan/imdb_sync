from collections import OrderedDict

df_options = OrderedDict()

df_options['titleprincipals'] = {
		'index': 'tconst',
		'columns': ['tconst', 'ordering', 'nconst', 'category', 'job', 'characters'],
		'dtype': {'tconst':'object', 'ordering':'int', 'nconst': 'object', 'category': 'object', 'job': 'object', 'characters': 'object'},
		'mapping': {'\\N': None}
	}