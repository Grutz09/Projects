import matplotlib as mpt
import geopandas as gpd
import matplotlib.pyplot as plt

full_data = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\DEC_lands\DEC_lands\DEC_lands.shp")

data = full_data.loc[:, ['CLASS', 'COUNTY', 'geometry']].copy()

wild_lands = data.loc[data.CLASS.isin(['WILD FOREST', 'WILDERNESS'])].copy()
# vsl = wild_lands.plot()

# print(wild_lands.geometry.head())

#campsite
POI_data = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\DEC_pointsinterest\DEC_pointsinterest\Decptsofinterest.shp")
campsites = POI_data.loc[POI_data.ASSET == 'PRIMITIVE CAMPSITE'].copy()

#footrails
road_trails = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\DEC_roadstrails\DEC_roadstrails\Decroadstrails.shp")
trails = road_trails.loc[road_trails.ASSET == 'FOOT TRAIL'].copy()

counties = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\NY_county_boundaries\NY_county_boundaries\NY_county_boundaries.shp")

#define basemap with country boundaries
ax = counties.plot(figsize=(10, 10), color = 'none', edgecolor='gainsboro', zorder=3)

#add wildlands, campsite, and footrails in basemap
wild_lands.plot(color='lightgreen', ax=ax)
campsites.plot(color='brown', markersize= 2, ax=ax)
trails.plot(color='black', markersize = 1, ax=ax) 

plt.show()


