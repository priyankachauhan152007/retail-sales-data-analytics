import pandas as pd

# Load the retail sales dataset
df = pd.read_csv("data/retail_sale.csv")

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Display basic dataset information
print("\n--- Dataset Information ---")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))

# Calculate total revenue
print("\n--- Overall Sales ---")
print("Total Revenue:", df["Total Amount"].sum())
print("Average Transaction Amount:", df["Total Amount"].mean())
print("Highest Transaction Amount:", df["Total Amount"].max())
print("Lowest Transaction Amount:", df["Total Amount"].min())

# Analyse sales by product category
print("\n--- Sales by Product Category ---")
category_sales = df.groupby("Product Category")["Total Amount"].sum()
print(category_sales.sort_values(ascending=False))

# Analyse quantity sold by category
print("\n--- Quantity Sold by Category ---")
category_quantity = df.groupby("Product Category")["Quantity"].sum()
print(category_quantity.sort_values(ascending=False))

# Analyse sales by gender
print("\n--- Sales by Gender ---")
gender_sales = df.groupby("Gender")["Total Amount"].sum()
print(gender_sales.sort_values(ascending=False))

# Analyse monthly sales
print("\n--- Monthly Sales ---")
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total Amount"].sum()
print(monthly_sales.sort_values(ascending=False))