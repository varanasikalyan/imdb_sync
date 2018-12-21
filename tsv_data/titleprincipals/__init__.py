import platform

if platform.sys.version_info.major < 3:
	from titleprincipalsloader import *
else:
	from .titleprincipalsloader import *