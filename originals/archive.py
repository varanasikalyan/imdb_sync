def extract_gz(source_file, target_file):
	from gzip import GzipFile
	in_file = GzipFile(source_file, 'rb')
	stream = in_file.read()
	
	out_file = file(target_file, 'wb')
	out_file.write(stream)
	out_file.close()
	in_file.close()
			
def extract_zip(source_zip, target_dir):
	from zipfile import ZipFile, extractall
	with ZipFile(source_zip,"r") as zip_ref:
		extractall(target_dir)