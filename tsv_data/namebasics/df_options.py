from collections import OrderedDict

df_options = OrderedDict()

df_options['namebasics'] = {
		'columns': ['nconst', 'primaryName', 'birthYear', 'deathYear'],
		'dtype': {'nconst':'object', 'primaryName':'object', 'birthYear': 'int', 'deathYear': 'int'},
		'mapping': {'\\N': 0}
	}

df_options['nameprimaryprofession'] = {
		'columns': ['nconst', 'primaryProfession'],
		'dtype': {'nconst':'object', 'primaryProfession':'object'},
		'mapping': {'\\N': None},
		'un_group_by':{'nconst': 'primaryProfession'}
	}

df_options['nameknownfortitles'] = {
		'columns': ['nconst', 'knownForTitles'],
		'dtype': {'nconst':'object', 'knownForTitles':'object'},
		'mapping': {'\\N': None},
		'un_group_by': {'nconst': 'knownForTitles'}
	}