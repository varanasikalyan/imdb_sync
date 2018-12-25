from .df_options import *
from root import engine
import config
import pandas as pd
import os
import gc
import sys

def load_tsv_to_sql(file, df_options=None):
    try:
        """Get path of the tsv file to load"""  
        tsv_path = get_tsv_path('tsv_data\\{0}'.format(file))

        for key, value in df_options.items():
            """Loading initial dataframe"""
            print('Pulling the latest data for table: {0} from tsv.'.format(key))
            count = 1
            for df in pd.read_csv(tsv_path, sep='\t', usecols=value['columns'], encoding='utf-8', chunksize=config.CHUNK_SIZE):
                sys.stdout.write("\rProcessing {0}K Rows   ".format((count * config.CHUNK_SIZE) / 1000))
                """Cleaning \\N values in year with None"""
                if 'mapping' in value.keys():
                    df = df.applymap(lambda s: value['mapping'].get(s) if s in value['mapping'] else s)

                """Set the appropriate datatypes to the columns"""
                df.astype(value['dtype'], copy=True)

                """Un Groupby column if required"""
                if 'un_group_by' in value.keys():
                    for iden, elem in value['un_group_by'].items():
                        df = df.drop(elem, axis=1).join(df[elem].str.split(",", expand = True).stack().reset_index(drop=True, level=1).rename(elem))

                """ReIndex the data frame"""                
                df.set_index(value['index'], inplace=True)
                
                """Dumping the data into database"""            
                df.to_sql(key, con=engine, if_exists='append')
            
                """Dispose dataframe"""
                del df
                gc.collect()
                count = count + 1
            sys.stdout.write("\n")
    except Exception as e:
        print("Unexpected error:", str(e))      
        raise
    else:
        pass
    finally:
        pass

def get_tsv_path(filename):
    folder = os.path.join(os.getcwd(), filename)
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".tsv"):
                return os.path.join(root, file)

load_tsv_to_sql('titleepisodes', df_options)