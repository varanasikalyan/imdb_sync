from collections import OrderedDict

df_options = OrderedDict()

df_options['titleratings'] = {
		'columns': ['tconst', 'averageRating', 'numVotes'],
		'dtype': {'tconst':'object', 'averageRating':'float', 'numVotes': 'int'},
		'mapping': {'\\N': 0}
	}