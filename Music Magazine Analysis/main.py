import pandas as pd
import sqlite3

con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")
artists = pd.read_sql("SELECT * FROM artists", con)
content = pd.read_sql("SELECT * FROM content", con)
genres = pd.read_sql("SELECT * FROM genres", con)
labels = pd.read_sql("SELECT * FROM labels", con)
reviews = pd.read_sql("SELECT * FROM reviews", con)

### ARTISTS' TABLE
missing_data = artists.isnull().sum()
rm_duplicate = artists.drop_duplicates(inplace=True)
artist_name = artists["artist"].str.title()

### CONTENT'S TABLE
missing = content.isnull().sum()
drop_dupli = content.drop_duplicates()


### GENRES'S TABLE
missing_data = genres.isnull().sum()
fill_data = genres["genre"].fillna('Unkown')

### LABELS
print(labels)
missing = labels.isnull().sum() #38 missing data from label column
fill_label = labels["label"].fillna('Unknown')

### REVIEWS
missing_authorType = reviews['author_type'].isnull().sum()
fill_auth_type = reviews['author_type'].fillna('contributor')
print(reviews.info())
# print(reviews.sort_values(by='reviewid',ascending=True))