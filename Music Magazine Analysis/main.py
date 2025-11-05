import pandas as pd
import sqlite3

con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")
df1 = pd.read_sql("SELECT * FROM artists", con)
df2 = pd.read_sql("SELECT * FROM content", con)
df3 = pd.read_sql("SELECT * FROM genres", con)
df4 = pd.read_sql("SELECT * FROM labels", con)
df5 = pd.read_sql("SELECT * FROM reviews", con)
df6 = pd.read_sql("SELECT * FROM years", con)

### ARTISTS' TABLE
df1 = df1.drop_duplicates().copy()
df1["artist"] = df1["artist"].str.title()
df1 = df1.sort_values(by=['reviewid'], ascending=True)

### CONTENT'S TABLE
df2 = df2.drop_duplicates().copy()
df2 = df2.sort_values(by=['reviewid'], ascending=True)

### GENRES'S TABLE
df3["genre"] = df3['genre'].str.title()
df3 = df3.fillna('Unknown')
df3 = df3.sort_values(by=['reviewid'], ascending=True)

### LABELS
df4.isnull().sum() #38 missing data from label column
df4['label'] = df4["label"].fillna('Unknown')
df4["label"] = df4["label"].str.title()
df4 = df4.sort_values(by=['reviewid'], ascending=True)

### REVIEWS
df5.isnull().any()
df5['author_type'] = df5["author_type"].fillna('Unkown')
df5['artist'] = df5["artist"].str.title()
df5['title'] = df5["title"].str.title()
df5 = df5.sort_values(by=['reviewid'], ascending=True)

high_scores = df5['artist'].loc[df5.score >= 8.5]
print(high_scores)


### YEARS
df6["year"] = df6.year.fillna(0).dropna()
df6["year"] = df6["year"].astype('int')
df6 = df6.sort_values(by=['reviewid'], ascending=True)

