import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/retail_sale.csv")

# Calculate total sales for each product category
category_sales = df.groupby("Product Category")["Total Amount"].sum()

# Create a bar chart
category_sales.plot(kind="bar")

# Add chart title and labels
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales (₹)")

# Display the category names horizontally
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("visualizations/category_sales.png", dpi=300, bbox_inches="tight")
plt.show(block=False)

# --------------------------------
# Chart 2: Sales Distribution by Gender
# --------------------------------

# Calculate total sales by gender
gender_sales = df.groupby("Gender")["Total Amount"].sum()

# Create a pie chart
plt.figure(figsize=(7, 7))
gender_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

# Add chart title
plt.title("Sales Distribution by Gender")

# Remove the default y-axis label
plt.ylabel("")

# Display the chart
plt.tight_layout()
plt.savefig("visualizations/gender_sales.png", dpi=300, bbox_inches="tight")
plt.show()
# --------------------------------
# Chart 3: Monthly Sales Trend
# --------------------------------

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Group sales by month
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total Amount"].sum()

# Create the line chart
plt.figure(figsize=(10, 5))
plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

# Add title and labels
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")

# Rotate month labels for readability
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()
plt.savefig("visualizations/monthly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.show()


