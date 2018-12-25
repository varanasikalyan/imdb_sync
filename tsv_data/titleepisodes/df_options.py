from collections import OrderedDict

df_options = OrderedDict()

df_options['titleepisodes'] = {
		'index': 'tconst',
		'columns': ['tconst', 'parentTconst', 'seasonNumber', 'episodeNumber'],
		'dtype': {'tconst':'object', 'parentTconst':'object', 'seasonNumber': 'int', 'episodeNumber': 'int'},
		'mapping': {'\\N': 0}
	}