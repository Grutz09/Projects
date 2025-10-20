import pandas as pd

df = pd.read_excel(r"C:\Users\seanandrew\Desktop\datasets\Customer Call List.xlsx")

# ## NOT WORKING 
# print(df.isnull().sum())
# df['Last_Name'] = df['Last_Name'].astype('str')
# df_fill = df['Last_Name'].fillna(df.mean(), inplace=True)
# print(df_fill)

### WORKING
# df_dupli = df.drop_duplicates()
# df1= df_dupli.drop(columns="Not_Useful_Column")


# df["Last_Name"] = df["Last_Name"].drop_duplicates()
# df['Last_Name'] = df["Last_Name"].str.strip("123_/.")
# print(df["Last_Name"])

df['Phone_Number'] = df["Phone_Number"].str.replace('[^0-9]','', regex=True)
print(df['Phone_Number'])