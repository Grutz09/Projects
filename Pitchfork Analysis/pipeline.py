import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import seaborn as sn
import numpy as np

# =======================  LOAD DATA  ===================================
con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")

reviews = pd.read_sql("SELECT * FROM reviews", con)
artists = pd.read_sql("SELECT * FROM artists", con)
genres = pd.read_sql("SELECT * FROM genres", con)
years = pd.read_sql("SELECT * FROM years", con)

# ======================= Descriptive Analysis ===============================
# let's drop null values and columns that are not necessary to the data we want to get
genres = genres.dropna().fillna(0)
reviews = reviews.drop(['author_type', 'url'], axis=1, inplace=False)

# # now that we are done wih cleaning we can proceed to finding joining genre column in reviews table
# s = reviews.groupby('score')
# score_agg = s['best_new_music'].agg(['sum', 'count']).reset_index()
# print(score_agg)

# plt.plot(score_agg['score'], score_agg['count'], label = 'All Reviews')
# plt.plot(score_agg['score'], score_agg['sum'], label = 'Best New Music')
# plt.legend(loc='best')
# plt.title('Score Distribution')
# plt.xlabel('score')
# plt.ylabel('reviews')
# # plt.show()

# genre_pubyear = pd.merge(genres, reviews[['pub_year', 'reviewid']])
# num_genres_year = genre_pubyear.groupby(['pub_year', 'genre']).agg({'reviewid': 'count'}).unstack()

# num_genres_year.columns = num_genres_year.columns.get_level_values(1)
# total_genre_year = num_genres_year.sum(axis=1)

# #calculate percentage of each genre after summing up
# ratio_total_genre_year = num_genres_year.divide(total_genre_year, axis=0)*100

# plt.figure(figsize=(12,6))
# plt.plot(num_genres_year.index, num_genres_year.values, linestyle='--')   
# plt.legend(["electronic", "experimental","folk/country", "global","jazz", "metal","pop/r&b", "rap", "rock"], loc='best')
# plt.title("Genre Reviews Distribution")
# plt.xlabel("Year")
# plt.ylabel("Reviews")

# #percentage of genre
# ax = sn.lineplot(data=ratio_total_genre_year)
# ax.set_xlabel('Year Review was Published')
# ax.set_ylabel('Percentage')
# ax.set_title('Percentage of Each Genre each Year')
# ax.legend(loc='right', bbox_to_anchor = (1.4, 0.5))
# plt.tight_layout()
# # plt.show()

# =================== ARTIST BASED INSIGHT =================

#let's find out how many best new music is there for every artists

artist_bestmusic_count = (reviews.groupby('artist', as_index=False).agg(best_new_music_count = ('best_new_music', 'count')).sort_values('best_new_music_count', ascending=False))

top_10_most_count = artist_bestmusic_count.iloc[0:10]

# plt.figure(figsize=(8,5))
# plt.barh(top_10_most_count['artist'], top_10_most_count['best_new_music_count'], color= 'skyblue')
# plt.xlabel('counts')
# plt.ylabel('artists')
# plt.title('Top 10 artist with most best new music')
# plt.show()

# now I'm gonna make a model to predict the score distribution of all artists
reviews['artist_popularity'] = reviews.groupby('artist')['artist'].transform('size').copy()
merged_df = pd.merge(reviews, genres, on='reviewid', how='left')

merged_df = pd.get_dummies(merged_df, columns=['genre'])


#collect genre columns
genre_cols = [col for col in merged_df.columns if col.startswith('genre_')]

#feature lists
score_features = ['artist_popularity', 'pub_year', 'best_new_music'] + genre_cols

# FEATURES
X = merged_df[score_features]
y = merged_df['score']

# SPLIT INTO TRAINING AND TESTING SETS
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#  CREATE AND TRAIN THE MODEL
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

#Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Coefficient (slope): ", model.coef_[0])
print("Model Intercept:", model.intercept_)
print("Mean Squared Error:",  mse)
print("r2 Score:", r2)

# Visualization (predicted vs actual)
plt.scatter(y_test, y_pred, color='blue', edgecolors='k')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')
plt.xlabel("Acutal Score")
plt.ylabel("Predicted Score")
plt.title("Score Prediction")
plt.show()