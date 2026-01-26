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
import seaborn as sn
import numpy as np

# =======================  LOAD DATA  ===================================
con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")

reviews = pd.read_sql("SELECT * FROM reviews", con)
artists = pd.read_sql("SELECT * FROM artists", con)
genres = pd.read_sql("SELECT * FROM genres", con)
years = pd.read_sql("SELECT * FROM years", con)

# ======================= Data Processing ===============================
# let's drop null values and columns that are not necessary to the data we want to get
genres = genres.dropna().fillna(0)
reviews = reviews.drop(['author_type', 'url'], axis=1, inplace=False)

# now that we are done wih cleaning we can proceed to finding joining genre column in reviews table
s = reviews.groupby('score')
score_agg = s['best_new_music'].agg(['sum', 'count']).reset_index()
print(score_agg)

plt.plot(score_agg['score'], score_agg['count'], label = 'All Reviews')
plt.plot(score_agg['score'], score_agg['sum'], label = 'Best New Music')
plt.legend(loc='best')
plt.title('Score Distribution')
plt.xlabel('score')
plt.ylabel('reviews')
# plt.show()

query = """
SELECT reviewid, score, genre
FROM reviews
    JOIN genres
        USING (reviewid)
"""
genre_score = pd.read_sql(query, con)
print(genre_score.describe())


genre_pubyear = pd.merge(genres, reviews[['pub_year', 'reviewid']])
num_genres_year = genre_pubyear.groupby(['pub_year', 'genre']).agg({'reviewid': 'count'}).unstack()

num_genres_year.column = num_genres_year.columns.get_level_values(1)
total_genre_year = num_genres_year.sum(axis=1)

plt.figure(figsize=(12,6))
plt.plot(num_genres_year.index, num_genres_year.values, linestyle='--')  
 
plt.legend(["electronic", "experimental","folk/country", "global","jazz", "metal","pop/r&b", "rap", "rock"], loc='best')
plt.title("Genre Reviews Distribution")
plt.xlabel("Year")
plt.ylabel("Reviews")
plt.show()

