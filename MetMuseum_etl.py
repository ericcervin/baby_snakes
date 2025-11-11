import pandas as pd
import sqlite3

def extract_from_csv(file_to_process): 
  dataframe = pd.read_csv(file_to_process,low_memory=False) 
  return dataframe

def load_csv(target_file, data): 
    data.to_csv(target_file)

    
def main():
   df = extract_from_csv("staging/MetObjects.csv")
   #use in BigQuery public data or download from https://github.com/metmuseum/openaccess
   #df.info()

   ny_df = df.query('City == "New York"')
   #ny_df.info()

   load_csv('databases/met_art_from_new_york.csv', ny_df)
   
   
main()
