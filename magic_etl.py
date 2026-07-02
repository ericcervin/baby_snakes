import pandas as pd
import sqlite3

def extract_from_csv(file_to_process): 
  dataframe = pd.read_csv(file_to_process) 
  return dataframe

def load_csv(target_file, data): 
    data.to_csv(target_file)

def load_sql(target_db,target_table, data):
    conn = sqlite3.connect(target_db)
    data.to_sql(target_table, conn, if_exists='replace', index=False)
    conn.close()
    
def main():
   df = extract_from_csv("staging/mtg-collection.csv")
   load_csv('databases/all_mtg.csv', df)
   load_sql('databases/mtg.db','release', df)
   df.info()
   
main()
