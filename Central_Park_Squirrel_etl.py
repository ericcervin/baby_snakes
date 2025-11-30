#https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data

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
   df = extract_from_csv("staging/2018_Central_Park_Squirrel_Data.csv")
   load_csv('databases/all_CP_Squirrels_2018.csv', df)
   load_sql('databases/all_CP_Squirrels_2018.db','squirrel', df)
   df.info()
   color_counts = df['Primary Fur Color'].value_counts(dropna=False)
   hectare_counts = df['Hectare'].value_counts(dropna=False)
   print(color_counts)
   print(hectare_counts)
main()
