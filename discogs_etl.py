import pandas as pd

def extract_from_csv(file_to_process): 
  dataframe = pd.read_csv(file_to_process) 
  return dataframe

def export_csv(target_file, data): 
    data.to_csv(target_file) 

def main():
   df = extract_from_csv("staging/discogs-collection.csv")
   export_csv('databases/all_discogs.csv', df)
   #df.info()
   
main()
