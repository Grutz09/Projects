import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

# =======================  LOAD DATA  ===================================
con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")

reviews = pd.read_sql("SELECT * FROM reviews", con)
artists = pd.read_sql("SELECT * FROM artists", con)
genres = pd.read_sql("SELECT * FROM genres", con)

# =======================  DAY 1 CLEANING  ===============================
reviews['pub_date'] = pd.to_datetime(reviews['pub_date'])
reviews['best_new_music'] = reviews['best_new_music'].astype(bool).astype(int)
reviews = reviews.drop_duplicates()
print(reviews.pub_date)

# =======================  DAY 2 MERGING  =================================
merged_df = reviews.merge(artists, on='reviewid', how='left', suffixes=('', '_artist'))

# combine genres per reviewid → "rock, pop, indie"
genres_combined = genres.groupby('reviewid')['genre'].apply(
    lambda x: ', '.join(x.dropna().astype(str))
).reset_index()

print(merged_df.columns)

merged_df = merged_df.merge(genres_combined, on='reviewid', how='left')
merged_df = merged_df.drop(['url'], axis=1)
merged_df.to_csv('merged_raw.csv', index=False)
print(merged_df.dtypes)
print(merged_df.isnull().sum())

# =======================  DAY 3 CLEANING  ===============================
merged_df['title'] = merged_df['title'].str.replace('--', '')
merged_df['score'] = pd.to_numeric(merged_df['score'])

merged_df = merged_df[(merged_df['score'] >= 0) & (merged_df['score'] <= 10)]

merged_df['artist'] = merged_df['artist'].str.lower().str.replace(r'[^a-z0-9\s]', '', regex=True)

# =======================  DAY 4 EDA  ====================================
score_counts = merged_df.groupby('pub_year')['score'].count()

plt.figure(figsize=(14, 5)) 

plt.subplot(2,2,1)
plt.bar(score_counts.index, score_counts.values, edgecolor='black')
plt.xlabel('year')
plt.ylabel('score')
plt.title('Artist Score Distribution')

# validate required columns
required_cols = {"reviewid", "pub_date"}
if not required_cols.issubset(merged_df.columns):
    raise ValueError(f"Missing required columns: {required_cols - set(merged_df.columns)}")

# ensure datetime conversion
try:
    merged_df['pub_date'] = pd.to_datetime(merged_df['pub_date'], errors="raise")
except Exception as e:
    raise ValueError(f"Invalid date format: {e}")

merged_df['year'] = merged_df['pub_date'].dt.year

reviews_per_year = merged_df.groupby('pub_year')["reviewid"].count().reset_index()

plt.subplot(2,2,2)
plt.bar(reviews_per_year['pub_year'], reviews_per_year['reviewid'], color='lightgreen', edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Number of Reviews')
plt.title('Reviews Per Year')

average_scores = merged_df.groupby('year')['score'].mean()

plt.subplot(2,2,3)
plt.bar(average_scores.index, average_scores.values, color='red', edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Average Score')
# plt.show()
# =======================  ARTIST INSIGHTS ===============================
artist_avg_score = merged_df.groupby(['artist']).score.mean()

sorted_artist = artist_avg_score.sort_values(ascending=False)
top_20_artist = sorted_artist.iloc[0:20]
bottom_20_artist = sorted_artist.iloc[-20:]

filtered_artist = merged_df[merged_df['artist'] == "massive attack"]
score_overtime = filtered_artist.groupby('pub_year')[['artist', 'score']].sum().reset_index()

krallis = merged_df[merged_df['artist'] == "krallice"]
grouped = krallis.groupby('pub_year')[['artist', 'score']].sum().reset_index()

uranium = merged_df[merged_df['artist'] == "uranium club"]
grouped1 = uranium.groupby('pub_year')[['artist', 'score']].sum().reset_index()

# =======================  GENRE & REVIEW INSIGHTS ========================

# Split combined genres → explode → average
merged_df['genres'] = merged_df['genre'].str.split(', ')
merged_df = merged_df.explode('genres')
merged_df = merged_df[merged_df['genres'].notna() & (merged_df['genres'].str.strip() != "")]

avg_score_genre = merged_df.groupby('genres')['score'].mean()
reviews_per_genre = merged_df.groupby('genres')['reviewid'].count()

plt.figure(figsize=(8,6))
plt.plot(avg_score_genre.index, avg_score_genre.values, marker='o', linestyle = '-' )
plt.title("Genre Trends")
plt.xlabel("Genre")
plt.ylabel("Average Score")
plt.grid(True)
# plt.show()

print(reviews_per_genre)

# ======================= ML-ready Dataset  ========================
genre_features = pd.get_dummies(merged_df['genres'], columns=['genres'], drop_first=True).astype(int)
numeric = pd.to_numeric(merged_df['author_type'], errors='coerce').fillna(0)
year = merged_df['pub_year']
month = merged_df['pub_month']
merged_df['score'] = merged_df['score'].dropna().fillna(0)

print(merged_df['score'].shape)
X = pd.concat([genre_features, numeric, year, month], axis=1)
y = merged_df['score']

print(f"Missing value in X: {X.isnull().sum()}")
print(f"Missing value in y: {y.isnull().sum()}")
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
    )

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

model = LinearRegression()
model.fit(X_train, y_train)
print(f"Intercept:,{ model.intercept_}")
print(f"Coefficient:, {model.coef_}")

# ======================== Evaluate Performance ===============================
y_pred = model.predict(X_test)

#calculate metrics
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae =  mean_absolute_error(y_test, y_pred)

print(f"Model Performance:")
print(f"R2 score: {r2:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"Mean: {mae:.3f}")


predictions = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(predictions.head())

#plot the actual data points
plt.scatter(X_test, y_test, color='blue', label='Actual')

#plot the reggression line
plt.plot([y_test.min(), y_test.max()], [], color='black', label='Regression Line')

plt.xlabel('review score')
plt.ylabel('score')
plt.title('Linear Regression')
plt.legend()
plt.show()
