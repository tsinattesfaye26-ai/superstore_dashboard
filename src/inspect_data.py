import pandas as pd


# Load raw data
df = pd.read_excel("data/raw/Sample_Superstore.xlsx")


print("\n========== SHAPE ==========")
print(df.shape)


print("\n========== COLUMNS ==========")
print(df.columns.tolist())


print("\n========== FIRST 5 ROWS ==========")
print(df.head())


print("\n========== DATA TYPES ==========")
print(df.dtypes)


print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


print("\n========== DUPLICATES ==========")
print("Duplicate rows:", df.duplicated().sum())


print("\n========== UNIQUE VALUES ==========")
print(df.nunique())


print("\n========== NUMERIC SUMMARY ==========")
print(df.describe())


print("\n========== CATEGORICAL SUMMARY ==========")
print(df.describe(include="object"))