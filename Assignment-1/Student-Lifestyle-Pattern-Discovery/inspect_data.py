import pandas as pd

df = pd.read_csv("students-productivity-dataset.csv")
print("Full Columns List:")
print(df.columns.tolist())
print("\nFirst row data:")
print(df.iloc[0].to_dict())
print("\nMissing values:")
print(df.isnull().sum())