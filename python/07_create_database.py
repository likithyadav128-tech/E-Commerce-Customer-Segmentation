import pandas as pd
import sqlite3

# ----------------------------------
# Load Clustered Dataset
# ----------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\clustered_customers.csv")

# ----------------------------------
# Create SQLite Database
# ----------------------------------

conn = sqlite3.connect(r"C:\Users\likit\OneDrive\Documents\E-Commerce-Customer-Segmentation\data\customer_segmentation.db")

df.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("Database Created Successfully!")