import sqlite3
import pandas as pd

def main():
    conn = sqlite3.connect('databases/discogs.db')
    df = pd.read_sql('SELECT * FROM release;',
            conn)
    df.to_csv('reports/all_releases.csv')

    df = pd.read_sql('''SELECT Artist,Count(*)
                        FROM release
                        GROUP BY Artist
                        ORDER BY Count(*) DESC ;''',
            conn)
    df.to_csv('reports/most_frequent_artists.csv')

main()
