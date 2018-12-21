import platform

if platform.sys.version_info.major < 3:
	from titleepisodesloader import *
else:
	from .titleepisodesloader import *