from collections import OrderedDict

def replace_is_original_title_null(val):
    if val == '\\N':
        return 1
    else:
        return val
        
df_options = OrderedDict()

df_options['titleakas'] = {
		'index': 'titleId',
		'columns': ['titleId', 'ordering', 'title', 'region', 'language', 'types', 'attributes', 'isOriginalTitle'],
		'dtype': {'titleId':'object', 'ordering':'int', 'title': 'object', 'region': 'object', 'language': 'object', 'types': 'object', 'attributes': 'object', 'isOriginalTitle': 'bool'},
		'mapping': {'\\N': 0, 1: True, 0: False},
		'converters': {'isOriginalTitle': replace_is_original_title_null}
	}