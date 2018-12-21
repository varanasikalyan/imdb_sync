import platform

if platform.sys.version_info.major < 3:
	from tsv_engine import *
else:
	from .tsv_engine import *

__all__ = ['namebasics', 'titleakas', 'titlebasics', 'titlecrew', 'titleepisodes', 'titleprincipals', 'titleratings']