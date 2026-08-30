import pandas as pd

# ----------------------------------
# Load Dataset
# ----------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\Mall_Customers.csv")

print("Dataset Loaded Successfully!")

# ----------------------------------
# Dataset Information
# ----------------------------------

print("\nDataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ----------------------------------
# Remove Duplicate Rows
# ----------------------------------

df = df.drop_duplicates()

# ----------------------------------
# Rename Columns
# ----------------------------------

df.columns = [
    "CustomerID",
    "Gender",
    "Age",
    "AnnualIncome",
    "SpendingScore"
]

print("\nUpdated Column Names:")
print(df.columns)

# ----------------------------------
# Save Cleaned Dataset
# ----------------------------------

save_path = r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\cleaned_mall_customers.csv"

df.to_csv(save_path, index=False)

print("\nCleaned dataset saved successfully!")
print("Location:", save_path)

print("\nData Cleaning Completed Successfully!")