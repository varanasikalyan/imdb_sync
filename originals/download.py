from .originals_config import *
from .archive import *
import requests
import gc
import sys

def download_data():
	try:
		for key, value in DATA_SOURCES['files'].items():
			file_name = '{0}{1}'.format(value, DATA_SOURCES['file_extension'])
			sys.stdout.write('Requesting download for {0}{1}\n'.format(value, DATA_SOURCES['file_extension']))

			r = requests.get('{0}{1}'.format(DATA_SOURCES['url'], file_name), stream = True)

			downloaded = 0

			with open('tsv_data\\{0}\\{1}'.format(key, file_name),"wb") as gz_file:
				for chunk in r.iter_content(chunk_size=1024):
				# writing one chunk at a time to gz_file file
					if chunk:
						gz_file.write(chunk)
						downloaded = downloaded + 1
						if(downloaded % 5000 == 0):
							sys.stdout.write("\rDownloaded {0}: {1} MB   ".format(value, round(downloaded / 1024, 3)))
							sys.stdout.flush()

				sys.stdout.write("\rDownloaded {0}: {1} MB   ".format(value, round(downloaded / 1024, 3)))
				gz_file.close()
				del gz_file
				gc.collect()

			sys.stdout.write('\n')
			del r
			gc.collect()
			extract_gz('tsv_data\\{0}\\{1}'.format(key, file_name), 'tsv_data\\{0}\\{1}'.format(key, value))

	except Exception as e:
		print("Unexpected error:", str(e))
		raise
	else:
		pass
	finally:
		pass

download_data()