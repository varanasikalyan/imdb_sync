import platform

if platform.sys.version_info.major < 3:
	from titleakasloader import *
else:
	from .titleakasloader import *