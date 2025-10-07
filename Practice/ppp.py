
import pandas as pd



wine = pd.read_csv(r"C:\Users\seanandrew\Desktop\kaggle_datasets\winemag-data-130k-v2.csv", index_col=0)
# ratio = (wine['points']/wine['price']).idxmax()
# bargain_wine = wine.loc[ratio, 'title']


tropical = wine['description'].map(lambda p: 'tropical' in p).sum()
fruity = wine['description'].map(lambda p: 'fruity' in p).sum()
descriptor_counts = pd.Series([tropical, fruity], index = ['tropical', 'fruity'])
print(descriptor_counts)