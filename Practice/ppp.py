import pandas as pd
import matplotlib
wine = pd.read_csv(r"C:\Users\seanandrew\Desktop\kaggle_datasets\winemag-data-130k-v2.csv", index_col=0)
# ratio = (wine['points']/wine['price']).idxmax()
# bargain_wine = wine.loc[ratio, 'title']


# tropical = wine['description'].map(lambda p: 'tropical' in p).sum()
# fruity = wine['description'].map(lambda p: 'fruity' in p).sum()
# descriptor_counts = pd.Series([tropical, fruity], index = ['tropical', 'fruity'])

# def score_rating(row):
#     if row == wine.loc[(wine.points >= 95) & (wine.country == 'Canada')]:
#         return "3 star"
#     elif row == wine.loc[wine.loc[wine.points >=85]]:
#         return "2 star"
#     elif row == wine.loc[wine.points < 85]:
#         return "1 star"
#     else:
#         return "Error"

# def score_rating2(row):
#     if row == wine.points >= 95 & wine.country == 'Canada':
#         return "3 star"
#     elif row == wine.points >=85:
#         return "2 star"
#     elif row == wine.points < 85:
#         return "1 star"
#     else:
#         return "Error"
    
# def score_rating3(row):

#     if row.country == ('Canada'):
#         return 'Three Star'
#     elif row.points >= 95:
#         return 'Three Star'
#     elif row.points >= 85:
#         return 'Two Star'
#     else:
#         return 'One Star'
   
# star_rating = wine.apply(score_rating3, axis='columns')

# print(wine.country.value_counts())
# countries_reviewed = wine.groupby(['country', 'province']).description.agg([len])
# mi = countries_reviewed.reset_index()

# countries_reviewed.sort_values(by='len')
# index = wine.sort_values(by=['variety', 'price'], ascending=False)

# wine[pd.isnull(wine.country)]
# # wine.region_2.fillna("Unknown")
# # print(wine.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))

# common_wines = wine['region_1'].fillna("Unknown").value_counts()
# reviews_per_region = common_wines.sort_values(ascending=False)

# wine.rename(columns={'points': 'score'})
# wine.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

# df = pd.DataFrame({
#     'ID': [1, 2, 3],
#     'Product': ['Asus', 'Lenovo', 'HP']
# })
# print(df)

import geopandas as gpd
import matplotlib.pyplot as plt

full_data = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\DEC_lands\DEC_lands\DEC_lands.shp")

data = full_data.loc[:, ['CLASS', 'COUNTY', 'geometry']].copy()

wild_lands = data.loc[data.CLASS.isin(['WILD FOREST', 'WILDERNESS'])].copy()
vsl = wild_lands.plot()

# print(wild_lands.geometry.head())

#campsite
POI_data = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\DEC_pointsinterest\DEC_pointsinterest\Decptsofinterest.shp")
campsites = POI_data.loc[POI_data.ASSET == 'PRIMITIVE CAMPSITE'].copy()

#footrails
road_trails = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\DEC_roadstrails\DEC_roadstrails\Decroadstrails.shp")
trails = road_trails.loc[road_trails.ASSET == 'FOOT TRAIL'].copy()

counties = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\NY_county_boundaries\NY_county_boundaries\NY_county_boundaries.shp")

#define basemap with country boundaries
ax = counties.plot(figsize=(10, 10), color = None, edgecolor='gainsboro', zorder=3)

#add wildlands, campsite, and footrails in basemap
wild_lands.plot(color='lightgreen', ax=ax)
campsites.plot(color='brown', markersize= 2, ax=ax)
trails.plot(color='black', markersize = 1, ax=ax) 
