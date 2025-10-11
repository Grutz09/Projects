import pandas as pd

wine = pd.read_csv(r"C:\Users\seanandrew\Desktop\kaggle_datasets\winemag-data-130k-v2.csv", index_col=0)
# ratio = (wine['points']/wine['price']).idxmax()
# bargain_wine = wine.loc[ratio, 'title']


# tropical = wine['description'].map(lambda p: 'tropical' in p).sum()
# fruity = wine['description'].map(lambda p: 'fruity' in p).sum()
# descriptor_counts = pd.Series([tropical, fruity], index = ['tropical', 'fruity'])

def score_rating(row):
    if row == wine.loc[(wine.points >= 95) & (wine.country == 'Canada')]:
        return "3 star"
    elif row == wine.loc[wine.loc[wine.points >=85]]:
        return "2 star"
    elif row == wine.loc[wine.points < 85]:
        return "1 star"
    else:
        return "Error"

def score_rating2(row):
    if row == wine.points >= 95 & wine.country == 'Canada':
        return "3 star"
    elif row == wine.points >=85:
        return "2 star"
    elif row == wine.points < 85:
        return "1 star"
    else:
        return "Error"
    
def score_rating3(row):

    if row.country == ('Canada'):
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
   

star_rating = wine.apply(score_rating3, axis='columns')
print(star_rating)