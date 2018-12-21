import platform

if platform.sys.version_info.major < 3:
	from titlebasicsloader import *
else:
	from .titlebasicsloader import *