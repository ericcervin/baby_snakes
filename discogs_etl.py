import pandas as pd

def extract_from_csv(file_to_process): 
  dataframe = pd.read_csv(file_to_process) 
  return dataframe

def main():
   df = extract_from_csv("staging/discogs-collection.csv")
   df.info()
   
main()
