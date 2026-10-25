import pandas as pd

# Load the retail sales dataset


df = pd.read_csv("data/retail_sale.csv")

# Display the first five records

print("\n--- First Five Records ---")
print(df.head())

# Display dataset dimensions

print("\n--- Dataset Dimensions ---")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Display column names and data types

print("\n--- Column Names and Data Types ---")
print(df.dtypes)

# Check missing values

print("\n--- Missing Values ---")
print(df.isnull().sum())

# Check duplicate records

print("\n--- Duplicate Records ---")
print("Number of duplicate rows:", df.duplicated().sum())

# Display statistical summary

print("\n--- Statistical Summary ---")
print(df.describe(include="all"))


# Step 5: Validate and prepare the dataset

# Convert Date column to datetime format

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Check whether any dates failed to convert

print("\n--- Invalid Dates ---")
print("Invalid date values:", df["Date"].isna().sum())

# Check for invalid numeric values

print("\n--- Numeric Validation ---")
print("Invalid ages:", ((df["Age"] < 0) | (df["Age"] > 120)).sum())
print("Invalid quantities:", (df["Quantity"] <= 0).sum())
print("Invalid prices:", (df["Price per Unit"] < 0).sum())
print("Invalid transaction amounts:", (df["Total Amount"] < 0).sum())

# Check the relationship between quantity, price and amount

df["Calculated Amount"] = df["Quantity"] * df["Price per Unit"]

print("\n--- Sales Amount Validation ---")
print("Rows where Total Amount differs from Quantity × Price per Unit:",
(df["Total Amount"] != df["Calculated Amount"]).sum())

# Display the updated data types

print("\n--- Updated Data Types ---")
print(df.dtypes)

# Display the prepared dataset

print("\n--- Prepared Dataset ---")
print(df.head())
