import sqlite3
import pandas as pd

def run_reporting():
   query = 'SELECT * FROM squirrel;'
   file = 'reports/central_park_squirrels/all_squirrels.csv'
   create_report(query,file) 

   query = '''SELECT
              COALESCE(NULLIF("Primary Fur Color", ''), 'Unknown') AS primary_color,
              "Highlight Fur Color" AS highlight_color,
              "Combination of Primary and Highlight Color"  AS combo_color,
              Count(*) AS 'squirrel_count'
              FROM squirrel
              GROUP BY combo_color
              ORDER BY squirrel_count DESC;
           '''
   file = 'reports/central_park_squirrels/squirrel_count_by_color.csv'
   create_report(query,file) 

def create_report(query,file):
    conn = sqlite3.connect('databases/all_CP_Squirrels_2018.db')
    df = pd.read_sql(query,conn)
    df.to_csv(file,index=False)
    conn.close()

def main():
    run_reporting()
    

main()
