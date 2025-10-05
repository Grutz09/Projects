import pandas as pd

# data = pd.DataFrame({'Samsung': ['Galaxy z21', 'A7 Note'], 
#                      'Oppo': ['A5', 'A16'] 
#                      }, index=['2020', '2021'])
# print(data)

# series = pd.Series([25000,23254,21200,26880], index=['2020 Revenue', '2021 Revenue', '2022 Revenue', '2023 Revenue'], name='Yearly Revenues')
# print(series)

wine_review = pd.read_csv(r"C:\Users\seanandrew\Desktop\kaggle_datasets\winemag-data-130k-v2.csv", index_col=0)

print(wine_review.loc[:5, ['taster_name', 'taster_twitter_handle']])   