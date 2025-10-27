import pandas as pd
import sqlite3

con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")
df1 = pd.read_sql("SELECT * FROM artists", con)
df2 = pd.read_sql("SELECT * FROM content", con)
df3 = pd.read_sql("SELECT * FROM genres", con)
df4 = pd.read_sql("SELECT * FROM labels", con)
df5 = pd.read_sql("SELECT * FROM reviews", con)

### ARTISTS' TABLE
df1 = df1.drop_duplicates().copy()
df1["artist"] = df1["artist"].str.title()

### CONTENT'S TABLE
df2 = df2.drop_duplicates().copy()

### GENRES'S TABLE
df3["genre"] = df3['genre'].str.title()
df3 = df3.fillna('Unknown')

### LABELS
df4.isnull().sum() #38 missing data from label column
df4['label'] = df4["label"].fillna('Unknown')
df4["label"] = df4["label"].str.title()

### REVIEWS
df5.isnull().any()
df5['author_type'] = df5["author_type"].fillna('Unkown')
df5['artist'] = df5["artist"].str.title()
df5['title'] = df5["title"].str.title()

print(df5)

