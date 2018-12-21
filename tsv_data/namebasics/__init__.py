import platform

if platform.sys.version_info.major < 3:
	from namebasicsloader import *
else:
	from .namebasicsloader import *