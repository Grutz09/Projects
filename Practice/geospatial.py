import matplotlib as mplt
import geopandas as gpd
import matplotlib.pyplot as plt

loans_filepath = gpd.read_file(r"C:\Users\seanandrew\Desktop\kaggle_datasets\archive (3)\kiva_loans\kiva_loans\kiva_loans.shp")

print(loans_filepath.head())

world_loans = gpd.read_file(loans_filepath)
# print(world_loans)
