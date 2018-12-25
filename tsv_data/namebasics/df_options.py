from collections import OrderedDict

df_options = OrderedDict()

df_options['namebasics'] = {
		'index': 'nconst',
		'columns': ['nconst', 'primaryName', 'birthYear', 'deathYear'],
		'dtype': {'nconst':'object', 'primaryName':'object', 'birthYear': 'int', 'deathYear': 'int'},
		'mapping': {'\\N': 0}
	}

df_options['nameprimaryprofession'] = {
		'index': 'nconst',
		'columns': ['nconst', 'primaryProfession'],
		'dtype': {'nconst':'object', 'primaryProfession':'object'},
		'mapping': {'\\N': None},
		'un_group_by':{'nconst': 'primaryProfession'}
	}

df_options['nameknownfortitles'] = {
		'index': 'nconst',
		'columns': ['nconst', 'knownForTitles'],
		'dtype': {'nconst':'object', 'knownForTitles':'object'},
		'mapping': {'\\N': None},
		'un_group_by': {'nconst': 'knownForTitles'}
	}