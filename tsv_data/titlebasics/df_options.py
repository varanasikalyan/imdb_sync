from collections import OrderedDict

df_options = OrderedDict()

df_options['titlebasics'] = {
		'columns': ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes'],
		'dtype': {'tconst':'object', 'titleType':'object', 'primaryTitle': 'object', 'originalTitle': 'object', 'isAdult': 'bool', 'startYear': 'int', 'endYear': 'int', 'runtimeMinutes': 'int'},
		'mapping': {'\\N': 0}
	}

df_options['titlebasicsgenres'] = {
		'columns': ['tconst', 'genres'],
		'dtype': {'tconst':'object', 'genres':'object'},
		'mapping': {'\\N': None},
		'un_group_by': {'tconst': 'genres'}
	}