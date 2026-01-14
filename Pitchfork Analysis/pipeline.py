import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

# =======================  LOAD DATA  ===================================
con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")

reviews = pd.read_sql("SELECT * FROM reviews", con)
artists = pd.read_sql("SELECT * FROM artists", con)
genres = pd.read_sql("SELECT * FROM genres", con)

# =======================  CLEANING  ===============================
reviews['pub_date'] = pd.to_datetime(reviews['pub_date'])
reviews['best_new_music'] = reviews['best_new_music'].astype(bool).astype(int)
reviews = reviews.drop_duplicates()

# ======================= MERGING  =================================
merged_df = reviews.merge(artists, on='reviewid', how='left', suffixes=('', '_artist'))

# combine genres per reviewid - "rock, pop, indie"
genres_combined = genres.groupby('reviewid')['genre'].apply(
    lambda x: ', '.join(x.dropna().astype(str))
).reset_index()

merged_df = merged_df.merge(genres_combined, on='reviewid', how='left')
merged_df = merged_df.drop(['url'], axis=1)

# =======================  FINAL CLEANING  ===============================
merged_df['title'] = merged_df['title'].str.replace('--', '')
merged_df['score'] = pd.to_numeric(merged_df['score'])

merged_df = merged_df[(merged_df['score'] >= 0) & (merged_df['score'] <= 10)]
merged_df['artist'] = merged_df['artist'].str.lower().str.replace(r'[^a-z0-9\s]', '', regex=True)

merged_df['pub_date'] = pd.to_datetime(merged_df['pub_date'])
merged_df['year'] = merged_df['pub_date'].dt.year
merged_df['month'] = merged_df['pub_date'].dt.month
merged_df['artist'] = merged_df['artist'].dropna()
merged_df = merged_df[merged_df['artist'].notna() & (merged_df['artist'].str.strip() != "")]
merged_df = merged_df[merged_df['genre'].notna() & (merged_df['genre'].str.strip() != "")]

# ======================= Score Distribution Analysis ================================
#data for histogram
artists_score = merged_df.groupby('artist')['score'].mean()

genre_score = merged_df.groupby('genre')['score'].max()

yearly_score = merged_df.groupby('pub_year')['score'].mean()


#plotting basic histogram
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.hist(artists_score, bins=20, color='blue', edgecolor='black')

#adding labels and title
plt.xlabel('Score')
plt.ylabel('Artist Counts')
plt.title('Artist Score')

plt.subplot(2,2,2)
plt.hist(genre_score, bins=20, color='red', edgecolor='black')
#adding labels and title
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Genre Score')

plt.subplot(2,2,3)
plt.plot(yearly_score.index,yearly_score.values, color='green')
#adding labels and title
plt.xlabel('Year')
plt.ylabel('Average Score')
plt.title('Yearly Score')

plt.tight_layout()
# plt.show()

# ======================= Top Artist and Genres ================================
#most reviewed artist
artists_score = merged_df.groupby('artist')['reviewid'].count()
top_genres = merged_df.groupby('genre')['genre'].count()

average_genre_score = merged_df.groupby('genre')['score'].mean()

top10_artist = artists_score.sort_values(ascending=False)
top10_artist = top10_artist.iloc[0:10]

# ======================= Trends Over Time ================================
reviews_per_year = merged_df.groupby('pub_year')['reviewid'].count()
reviews_per_year = reviews_per_year.sort_values(ascending=False)

average_score_per_year = merged_df.groupby('pub_year')['score'].mean()

plt.figure(figsize=(10,6))
plt.plot(average_score_per_year.index, average_score_per_year.values, color='blue')

plt.xlabel('Year')
plt.ylabel('Avg Score')
plt.title('Average Score Per Year')
plt.tight_layout()
plt.show()

# ================= Score Category Prediction (Classification) ====================
merged_df['artist'] = merged_df.groupby('artist')['reviewid'].count().copy()
y = merged_df['score']

print(merged_df.info())
score_features = ['genre', 'pub_year', 'artist']

# ======================= PREVENT DATA LEAKAGE ===========================

# unique_reviews = merged_df.drop_duplicates(subset='reviewid')

# train_ids, test_ids = train_test_split(
#     unique_reviews['reviewid'],
#     test_size= 0.2,
#     random_state=42
# )

# train_df = merged_df[merged_df['reviewid'].isin(train_ids)].copy()
# test_df = merged_df[merged_df['reviewid'].isin(test_ids)].copy()

# ======================= GENRE ENCODING ================================
# train_df['genres'] = train_df['genre'].str.split(', ')
# test_df['genres'] = test_df['genre'].str.split(', ')

# train_df = train_df.explode('genres')
# test_df = test_df.explode('genres')

# genre_dummies_train = pd.get_dummies(train_df['genres'], prefix='genre')
# genre_dummies_test = pd.get_dummies(test_df['genres'], prefix='genre')

# #align columns
# genre_dummies_train, genre_dummies_test = genre_dummies_train.align(
#     genre_dummies_test, join='left', axis=1, fill_value=0
# )

# ======================= FEATURES AND TARGET ================================
# X_train = pd.concat([
#     genre_dummies_train,
#     train_df[['year', 'month']]
#     ], axis=1)

# X_test = pd.concat([
#     genre_dummies_test,
#     test_df[['year', 'month']]
#     ], axis=1
# )

# y_train = train_df['score']
# y_test = test_df['score']

# ======================= MODEL PIPELINE ================================
# pipeline = Pipeline([
#     ('scaler', StandardScaler()),
#     ('model', RandomForestRegressor(
#         n_estimators=200,
#         random_state=42,
#         n_jobs=1))
# ])

# pipeline.fit(X_train, y_train)

# # ======================= EVALUATION ====================================
# y_pred = pipeline.predict(X_test)

# r2 = r2_score(y_test, y_pred)
# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# mae = mean_absolute_error(y_test, y_pred)

# print("Model Performance")
# print(f"R2 Score : {r2:.3f}")
# print(f"RMSE     : {rmse:.3f}")
# print(f"MAE      : {mae:.3f}")

# ======================= VISUALIZATION ====================================
# plt.figure(figsize=(6,6))
# plt.scatter(y_test, y_pred, alpha=0.5)
# plt.plot([0,10], [0,10], 'k--')
# plt.xlabel("Actual Score")
# plt.ylabel("Predicted Score")
# plt.title("Review Score Prediction")
# plt.show()

# # =======================  DAY 4 EDA  ====================================
# score_counts = merged_df.groupby('pub_year')['score'].count()

# plt.figure(figsize=(14, 5)) 

# plt.subplot(2,2,1)
# plt.bar(score_counts.index, score_counts.values, edgecolor='black')
# plt.xlabel('year')
# plt.ylabel('score')
# plt.title('Artist Score Distribution')

# # validate required columns
# required_cols = {"reviewid", "pub_date"}
# if not required_cols.issubset(merged_df.columns):
#     raise ValueError(f"Missing required columns: {required_cols - set(merged_df.columns)}")

# # ensure datetime conversion
# try:
#     merged_df['pub_date'] = pd.to_datetime(merged_df['pub_date'], errors="raise")
# except Exception as e:
#     raise ValueError(f"Invalid date format: {e}")

# merged_df['year'] = merged_df['pub_date'].dt.year

# reviews_per_year = merged_df.groupby('pub_year')["reviewid"].count().reset_index()

# plt.subplot(2,2,2)
# plt.bar(reviews_per_year['pub_year'], reviews_per_year['reviewid'], color='lightgreen', edgecolor='black')
# plt.xlabel('Year')
# plt.ylabel('Number of Reviews')
# plt.title('Reviews Per Year')

# average_scores = merged_df.groupby('year')['score'].mean()

# plt.subplot(2,2,3)
# plt.bar(average_scores.index, average_scores.values, color='red', edgecolor='black')
# plt.xlabel('Year')
# plt.ylabel('Average Score')
# # plt.show()
# # =======================  ARTIST INSIGHTS ===============================
# artist_avg_score = merged_df.groupby(['artist']).score.mean()

# sorted_artist = artist_avg_score.sort_values(ascending=False)
# top_20_artist = sorted_artist.iloc[0:20]
# bottom_20_artist = sorted_artist.iloc[-20:]

# filtered_artist = merged_df[merged_df['artist'] == "massive attack"]
# score_overtime = filtered_artist.groupby('pub_year')[['artist', 'score']].sum().reset_index()

# krallis = merged_df[merged_df['artist'] == "krallice"]
# grouped = krallis.groupby('pub_year')[['artist', 'score']].sum().reset_index()

# uranium = merged_df[merged_df['artist'] == "uranium club"]
# grouped1 = uranium.groupby('pub_year')[['artist', 'score']].sum().reset_index()

# # =======================  GENRE & REVIEW INSIGHTS ========================

# # Split combined genres → explode → average
# unique_reviews = merged_df.drop_duplicates(subset='reviewid')

# merged_df['genre'] = merged_df['genre'].str.split(', ')
# merged_df['genre'] = merged_df.explode('genre')
# merged_df = merged_df[merged_df['genres'].notna() & (merged_df['genres'].str.strip() != "")]

# avg_score_genre = merged_df.groupby('genres')['score'].mean()
# reviews_per_genre = merged_df.groupby('genres')['reviewid'].count()

# plt.figure(figsize=(8,6))
# plt.plot(avg_score_genre.index, avg_score_genre.values, marker='o', linestyle = '-' )
# plt.title("Genre Trends")
# plt.xlabel("Genre")
# plt.ylabel("Average Score")
# plt.grid(True)
# # plt.show()

# print(reviews_per_genre)

# # ======================= ML-ready Dataset  ========================
# genre_features = pd.get_dummies(merged_df['genres'], columns=['genres'], drop_first=True).astype(int)
# numeric = pd.to_numeric(merged_df['author_type'], errors='coerce').fillna(0)
# year = merged_df['pub_year']
# month = merged_df['pub_month']
# merged_df['score'] = merged_df['score'].fillna(0)

# print(merged_df['score'].shape)
# X = pd.concat([genre_features, numeric, year, month], axis=1)
# y = merged_df['score']

# print(f"Missing value in X: {X.isnull().sum()}")
# print(f"Missing value in y: {y.isnull().sum()}")
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.2,
#     random_state=42
#     )

# print(f"Training set size: {X_train.shape[0]}")
# print(f"Testing set size: {X_test.shape[0]}")

# model = LinearRegression()
# model.fit(X_train, y_train)
# print(f"Intercept:,{ model.intercept_}")
# print(f"Coefficient:, {model.coef_}")

# # ======================== Evaluate Performance ===============================
# y_pred = model.predict(X_test)

# #calculate metrics
# r2 = r2_score(y_test, y_pred)
# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# mae =  mean_absolute_error(y_test, y_pred)

# print(f"Model Performance:")
# print(f"R2 score: {r2:.3f}")
# print(f"RMSE: {rmse:.3f}")
# print(f"Mean: {mae:.3f}")


# predictions = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
# print(predictions.head())

# #plot the actual data points
# plt.scatter(y_test, y_pred, color='blue', label='Actual')

# #plot the reggression line
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, color='black', label='Perfect Prediction')

# plt.xlabel('review score')
# plt.ylabel('score')
# plt.title('Linear Regression')
# plt.legend()
# plt.show()
