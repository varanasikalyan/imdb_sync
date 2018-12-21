from root import engine
import pandas as pd
import os
import gc
import datetime

def load_tsv_to_sql(file):
	print('{0}: Pulling the latest tsv for {1}.'.format(datetime.datetime.now(), file))
	tsv_path = get_tsv_path('tsv_data\\{0}'.format(file))
	df = pd.read_csv(tsv_path, sep='\t', encoding='latin-1')
	print('{0}: Dumping the latest tsv for {1} into db.'.format(datetime.datetime.now(), file))
	df.to_sql(file, con=engine, if_exists='replace')
	del df
	gc.collect()


def get_tsv_path(file):	
	folder = os.path.join(os.getcwd(), file)	
	return os.path.join(folder, os.listdir(folder)[0])