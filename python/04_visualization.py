import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\cleaned_mall_customers.csv")

print("Dataset Loaded Successfully!")

sns.set_style("whitegrid")

# ---------------------------------
# Gender Distribution
# ---------------------------------

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender")
plt.title("Gender Distribution")
plt.tight_layout()
plt.show()

# ---------------------------------
# Age vs Spending Score
# ---------------------------------

plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x="Age", y="SpendingScore", hue="Gender")
plt.title("Age vs Spending Score")
plt.tight_layout()
plt.show()

# ---------------------------------
# Annual Income vs Spending Score
# ---------------------------------

plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x="AnnualIncome", y="SpendingScore", hue="Gender")
plt.title("Annual Income vs Spending Score")
plt.tight_layout()
plt.show()

# ---------------------------------
# Spending Score by Gender
# ---------------------------------

plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Gender", y="SpendingScore")
plt.title("Spending Score by Gender")
plt.tight_layout()
plt.show()

# ---------------------------------
# Annual Income by Gender
# ---------------------------------

plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Gender", y="AnnualIncome")
plt.title("Annual Income by Gender")
plt.tight_layout()
plt.show()

# ---------------------------------
# Pair Plot
# ---------------------------------

sns.pairplot(
    df,
    vars=["Age", "AnnualIncome", "SpendingScore"],
    hue="Gender"
)

plt.show()

print("\nVisualization Completed Successfully!")