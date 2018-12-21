import platform

if platform.sys.version_info.major < 3:
	from titlecrewloader import *
else:
	from .titlecrewloader import *