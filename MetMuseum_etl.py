import pandas as pd
import sqlite3

def extract_from_csv(file_to_process): 
  dataframe = pd.read_csv(file_to_process) 
  return dataframe

    
def main():
   df = extract_from_csv("staging/MetObjects.csv")
   #use in BigQuery public data or download from https://github.com/metmuseum/openaccess
   df.info()
   
main()
