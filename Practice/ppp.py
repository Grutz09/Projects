
import pandas as pd



wine = pd.read_csv(r"C:\Users\seanandrew\Desktop\kaggle_datasets\winemag-data-130k-v2.csv", index_col=0)
# ratio = (wine['points']/wine['price']).idxmax()
# bargain_wine = wine.loc[ratio, 'title']


# tropical = wine['description'].map(lambda p: 'tropical' in p).sum()
# fruity = wine['description'].map(lambda p: 'fruity' in p).sum()
# descriptor_counts = pd.Series([tropical, fruity], index = ['tropical', 'fruity'])

three_star = wine['points'].loc[(wine.points >= 95) | (wine.country == 'Canada')].map(wine)
two_star = wine['points'].loc[wine.points >=85].map(wine)
one_star = wine['points'].loc[wine.points < 85].map(wine)

star_rating = pd.Series([three_star, two_star, one_star], index=['3 Star', '2 Star', '1 Star'])
print(star_rating[:10])