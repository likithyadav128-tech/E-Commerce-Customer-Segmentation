import pandas as pd

# ---------------------------------
# Load Clustered Dataset
# ---------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\clustered_customers.csv")

print("Clustered Dataset Loaded Successfully!\n")

# ---------------------------------
# Number of Customers in Each Cluster
# ---------------------------------

print("Customers in Each Cluster:\n")

print(df["Cluster"].value_counts().sort_index())

# ---------------------------------
# Average Values by Cluster
# ---------------------------------

print("\nCluster Summary:\n")

summary = df.groupby("Cluster")[["Age","AnnualIncome","SpendingScore"]].mean()

print(summary)

# ---------------------------------
# Save Summary
# ---------------------------------

summary.to_csv(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\cluster_summary.csv")

print("\nCluster Summary Saved Successfully!")

print("\nLocation:")

print(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\dataset\cluster_summary.csv")