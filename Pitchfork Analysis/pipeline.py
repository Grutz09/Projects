import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")

reviews = pd.read_sql("SELECT * FROM reviews", con)
artists = pd.read_sql("SELECT * FROM artists", con)
genres = pd.read_sql("SELECT * FROM genres", con)

#Day 1
reviews['pub_date'] = pd.to_datetime(reviews['pub_date'])
reviews['best_new_music'] = reviews['best_new_music'].astype('bool')
reviews['best_new_music'] = reviews['best_new_music'].replace({True: 1, False: 0})
reviews = reviews.drop_duplicates()

#Day 2 Join Extra Tables
merged_df = reviews.merge(artists, on='reviewid', how='left', suffixes=('', '_artist'))
genres_combined = genres.groupby('reviewid')['genre'].apply(
    lambda x: ', '.join(x.dropna().astype(str))).reset_index()

merged_df = merged_df.merge(genres_combined, on='reviewid', how='left')
merged_df.to_csv('merged_raw.csv', index=False)

print(merged_df.head())