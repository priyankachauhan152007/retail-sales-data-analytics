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
