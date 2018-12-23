def extract_gz(source_file, target_file):
	from shutil import copyfile
	copyfile(source_file, target_file)
			
def extract_zip(source_zip, target_dir):
	from zipfile import ZipFile, extractall
	with ZipFile(source_zip,"r") as zip_ref:
		extractall(target_dir)