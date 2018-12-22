from collections import OrderedDict

df_options = OrderedDict()

df_options['titleakas'] = {
		'columns': ['titleId', 'ordering', 'title', 'region', 'language', 'types', 'attributes', 'isOriginalTitle'],
		'dtype': {'titleId':'object', 'ordering':'int', 'title': 'object', 'region': 'object', 'language': 'object', 'types': 'object', 'attributes': 'object', 'isOriginalTitle': 'bool'},
		'mapping': {'\\N': 0, 1: True, 0: False}
	}