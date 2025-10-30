import sqlite3
import pandas as pd

def run_reporting():
    
    query = 'SELECT * FROM release;'
    file = 'reports/all_releases.csv'
    create_report(query,file)

    query = 'SELECT Artist,Count(*) FROM release GROUP BY Artist ORDER BY Count(*) DESC ;'
    file = 'reports/most_frequent_artists.csv'
    create_report(query,file)

    query = 'SELECT Label,Count(*) FROM release GROUP BY Label ORDER BY Count(*) DESC ;'
    file = 'reports/most_frequent_labels.csv'
    create_report(query,file)

def create_report(query,file):
    conn = sqlite3.connect('databases/discogs.db')
    df = pd.read_sql(query,conn)
    df.to_csv(file)
    conn.close()

def main():
    run_reporting()
    

main()
