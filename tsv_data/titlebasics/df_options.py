from collections import OrderedDict

def runtime_minutes(val):
	if val == '\\N':
		return 0
	else:
		return val

def start_year(val):
	if val == '\\N':
		return 0
	else:
		return val

def end_year(val):
	if val == '\\N':
		return 9999
	else:
		return val

def genres(val):
	if val == '\\N':
		return None
	else:
		return val

df_options = OrderedDict()

df_options['titlebasics'] = {
		'index': 'tconst',
		'columns': ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes'],
		'dtype': {'tconst':'object', 'titleType':'object', 'primaryTitle': 'object', 'originalTitle': 'object', 'isAdult': 'bool', 'startYear': 'object', 'endYear': 'object', 'runtimeMinutes': 'object'},
		'mapping': {'\\N': 0},
		'converters': {'startYear': start_year, 'endYear': end_year, 'runtimeMinutes': runtime_minutes}
	}

df_options['titlebasicsgenres'] = {
		'index': 'tconst',
		'columns': ['tconst', 'genres'],
		'dtype': {'tconst':'object', 'genres':'object'},
		'un_group_by': {'tconst': 'genres'},
		'converters': {'genres': genres}
	}