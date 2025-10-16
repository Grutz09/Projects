import matplotlib as mplt
import geopandas as gpd
import matplotlib.pyplot as plt
import fiona
fiona.supported_drivers['KML'] = 'rw'



loans_filepath = r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\kiva_loans\kiva_loans\kiva_loans.shp"

world_loans = gpd.read_file(loans_filepath)

PHL_loans = world_loans.loc[world_loans.country == 'Philippines'].copy()

PHL = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\Philippines_AL258.kml", driver='KML')
print(PHL.head())

ax = PHL.plot(figsize=(12,12), color='none', linestyle='-', edgecolor='gainsboro')
PHL_loans.plot(color='maroon', markersize=2, ax=ax)

plt.show()