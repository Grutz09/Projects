import pandas as pd

df = pd.read_excel(r"C:\Users\seanandrew\Desktop\datasets\Customer Call List.xlsx")
df_rmdupli = df.drop_duplicates()
print(df_rmdupli.Last_Name)
