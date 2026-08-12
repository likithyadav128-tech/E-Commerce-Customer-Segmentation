import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\cleaned_mall_customers.csv")

print("Dataset Loaded Successfully!")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

# ---------------------------------
# Gender Distribution
# ---------------------------------

plt.figure(figsize=(6,4))
sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")
plt.show()

# ---------------------------------
# Age Distribution
# ---------------------------------

plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=15)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Customers")
plt.show()

# ---------------------------------
# Annual Income Distribution
# ---------------------------------

plt.figure(figsize=(6,4))
plt.hist(df["AnnualIncome"], bins=15)
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Customers")
plt.show()

# ---------------------------------
# Spending Score Distribution
# ---------------------------------

plt.figure(figsize=(6,4))
plt.hist(df["SpendingScore"], bins=15)
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Customers")
plt.show()

# ---------------------------------
# Correlation Heatmap
# ---------------------------------

plt.figure(figsize=(6,5))

corr = df[["Age","AnnualIncome","SpendingScore"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

print("\nEDA Completed Successfully!")