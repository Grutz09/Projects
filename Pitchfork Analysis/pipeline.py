import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import seaborn as sns

con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")

reviews = pd.read_sql("SELECT * FROM reviews", con)
artists = pd.read_sql("SELECT * FROM artists", con)
genres = pd.read_sql("SELECT * FROM genres", con)

#Day 1
reviews['pub_date'] = pd.to_datetime(reviews['pub_date'])
# print(reviews[['title', 'artist', 'score']].isnull().sum())

reviews['best_new_music'] = reviews['best_new_music'].astype('bool')
reviews['best_new_music'] = reviews['best_new_music'].astype(int)
reviews = reviews.drop_duplicates()

#Day 2 Join Extra Tables
merged_df = reviews.merge(artists, on='reviewid', how='left', suffixes=('', '_artist'))
genres_combined = genres.groupby('reviewid')['genre'].apply(
    lambda x: ', '.join(x.dropna().astype(str))).reset_index()

merged_df = merged_df.merge(genres_combined, on='reviewid', how='left')
# merged_df.to_csv('merged_raw.csv', index=False)

#Day 3 Clean Merged Table
merged_df['title'] = merged_df['title'].str.replace('--', '')
merged_df['score'] = pd.to_numeric(merged_df['score'])

merged_df = merged_df[(merged_df['score'] >= 0) & (merged_df['score'] <= 10)]
merged_df['artist'] = merged_df['artist'].str.lower().str.replace(r'[^a-z0-9\s]', '', regex=True)

#Day 4 EDA Charts

## Score distribution
score_counts = merged_df.groupby('pub_year')['score'].count()

plt.figure(figsize=(14, 5)) 
plt.subplot(2,2,1)
plt.bar(score_counts.index, score_counts.values, edgecolor='black')
plt.xlabel('scores')
plt.ylabel('frequency')
plt.title('Artist Score Distribution')

## number of reviews per year
required_cols = {"reviewid", "pub_date"}
if not required_cols.issubset(merged_df.columns):
    raise ValueError(f"Missing required columns: {required_cols - set(merged_df.columns)}")

#convert date to datetime
try:
    merged_df['pub_date'] = pd.to_datetime(merged_df['pub_date'], errors="raise")
except Exception as e:
    raise ValueError(f"Invalid date format: {e}")

#extract year
merged_df['year'] = merged_df['pub_date'].dt.year

#aggregate reviews per year
reviews_per_year = merged_df.groupby('pub_year')["reviewid"].count().reset_index()

#plot
plt.subplot(2,2,2)
plt.bar(reviews_per_year['pub_year'], reviews_per_year['reviewid'], color='lightgreen', edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Number of Reviews')
plt.title('Reviews Per Year')

# Average score by year
average_scores = merged_df.groupby('year')['score'].mean()

plt.subplot(2,2,3)
plt.bar(average_scores.index, average_scores.values, color='red', edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Average Score')

#show plot
# plt.tight_layout()
# plt.show()

#Artist Based Insight 
artist_avg_score = merged_df.groupby(['artist']).score.mean()
#first sort the artist by score from top to bottom
sorted_artist = artist_avg_score.sort_values(ascending=False)
top_20_artist = sorted_artist.iloc[0:20]
bottom_20_artist = sorted_artist.iloc[-20:]

## get the artist score
filtered_artist = merged_df[merged_df['artist'] == "massive attack"]
score_overtime = filtered_artist.groupby('pub_year')[['artist', 'score']].sum().reset_index()
#plot
plt.figure(figsize=(12, 6))
plt.bar(score_overtime['pub_year'], score_overtime['score'], edgecolor='black')
plt.xlabel('year')
plt.ylabel('score')
plt.tight_layout()
plt.show()