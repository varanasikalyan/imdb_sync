import platform

if platform.sys.version_info.major < 3:
	from titleratingsloader import *
else:
	from .titleratingsloader import *