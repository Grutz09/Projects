import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")

reviews = pd.read_sql("SELECT * FROM reviews", con)

reviews['pub_date'] = pd.to_datetime(reviews['pub_date'])
reviews['best_new_music'] = reviews['best_new_music'].astype('bool')
reviews = reviews.drop_duplicates()
print(reviews.isnull().sum())