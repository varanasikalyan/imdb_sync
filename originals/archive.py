import sys

def extract_gz(source_file, target_file):
	from gzip import open as gopen
	from shutil import copyfileobj
	with gopen(source_file, 'rb') as f_in:
		sys.stdout.write('Extracting download file {0}\n'.format(source_file))
		with open(target_file, 'wb') as f_out:
			sys.stdout.write('Writing download file to {0}\n\n'.format(target_file))
			copyfileobj(f_in, f_out)	
			
def extract_zip(source_zip, target_dir):
	from zipfile import ZipFile, extractall
	with ZipFile(source_zip,"r") as zip_ref:
		extractall(target_dir)