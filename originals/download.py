from .originals_config import *
import requests
import gc
import sys

def download_data():
	for file in DATA_SOURCES['files']:
		file_name = '{0}{1}'.format(file, DATA_SOURCES['file_extension'])
		sys.stdout.write('Requesting download for {0}{1}\n'.format(file, DATA_SOURCES['file_extension']))

		r = requests.get('{0}{1}'.format(DATA_SOURCES['url'], file_name), stream = True)

		downloaded = 0

		with open('{0}\\{1}'.format('originals\\files', file_name),"wb") as gz_file:
			for chunk in r.iter_content(chunk_size=1024):
			# writing one chunk at a time to gz_file file
				if chunk:
					gz_file.write(chunk)
					downloaded = downloaded + 1
					if(downloaded % 5000 == 0):
						sys.stdout.write("\rDownloaded {0}: {1} MB ".format(file_name, round(downloaded / 1024, 3)))
						sys.stdout.flush()

			sys.stdout.write("\rDownloaded {0}: {1} MB".format(file_name, round(downloaded / 1024, 3)))
			del gz_file
			gc.collect()

		sys.stdout.write('\n\n')
		del r
		gc.collect()