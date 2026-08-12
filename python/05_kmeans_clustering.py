import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\cleaned_mall_customers.csv")

print("Dataset Loaded Successfully!")

# ---------------------------------
# Select Features
# ---------------------------------

X = df[["AnnualIncome", "SpendingScore"]]

# ---------------------------------
# Elbow Method
# ---------------------------------

wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        init="k-means++",
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8,5))

plt.plot(range(1,11), wcss, marker="o")

plt.title("Elbow Method")

plt.xlabel("Number of Clusters")

plt.ylabel("WCSS")

plt.grid(True)

plt.show()

# ---------------------------------
# Train KMeans
# ---------------------------------

kmeans = KMeans(
    n_clusters=5,
    init="k-means++",
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X)

print("\nClusters Created Successfully!")

print(df.head())

# ---------------------------------
# Cluster Visualization
# ---------------------------------

plt.figure(figsize=(8,6))

plt.scatter(
    df["AnnualIncome"],
    df["SpendingScore"],
    c=df["Cluster"],
    cmap="viridis",
    s=60
)

plt.xlabel("Annual Income (k$)")

plt.ylabel("Spending Score")

plt.title("Customer Segmentation using K-Means")

plt.colorbar(label="Cluster")

plt.grid(True)

plt.show()

# ---------------------------------
# Save Clustered Dataset
# ---------------------------------

save_path = r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\clustered_customers.csv"

df.to_csv(save_path, index=False)

print("\nClustered dataset saved successfully!")

print(save_path)