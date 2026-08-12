import pandas as pd

# ----------------------------
# Load Dataset
# ----------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\Mall_Customers.csv")

print("Dataset Loaded Successfully!")

print("\nShape of Dataset:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())