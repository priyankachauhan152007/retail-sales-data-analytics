# Retail Sales Data Analytics and Business Intelligence Dashboard

## 1. Project Overview

This project analyses retail sales data to understand sales performance, product category trends, customer purchasing patterns, and monthly sales changes. Python is used for data inspection, exploratory data analysis, and visualizations, while Power BI is used to create an interactive business intelligence dashboard.

## 2. Problem Statement

Retail businesses need to understand which product categories generate the most revenue, how customers contribute to sales, and how sales change over time. This project uses retail transaction data to identify useful patterns and support data-driven business decisions.

## 3. Project Objectives

* Inspect and prepare the retail sales dataset.
* Check missing values, duplicate records, and invalid data.
* Perform exploratory data analysis.
* Create meaningful visualizations.
* Develop an interactive Power BI dashboard.
* Identify business insights and provide recommendations.

## 4. Dataset Description

The dataset contains 1,000 retail transactions and nine original columns:

* Transaction ID
* Date
* Customer ID
* Gender
* Age
* Product Category
* Quantity
* Price per Unit
* Total Amount

**Dataset file:** `data/retail_sale.csv`

## 5. Tools and Technologies

* Python
* Pandas
* Matplotlib
* Power BI Desktop
* Git and GitHub
* Visual Studio Code

## 6. Data Cleaning and Preparation

The dataset was inspected for missing values, duplicate records, data types, and invalid values.

The checks found:

* 1,000 records and nine original columns.
* No missing values.
* No duplicate full rows.
* No invalid dates.
* No ages outside the checked range of 0–120.
* No non-positive quantities.
* No negative prices or total amounts.
* No mismatches between Total Amount and Quantity multiplied by Price per Unit.

The Date column was converted to a datetime format for time-based analysis.

## 7. Exploratory Data Analysis

The analysis examined:

* Total and average transaction sales.
* Highest and lowest transaction amounts.
* Sales by product category.
* Quantity sold by product category.
* Sales by gender.
* Monthly sales trends.

### Key results

* Total sales: ₹456,000.
* Average transaction amount: ₹456.
* Highest transaction amount: ₹2,000.
* Lowest transaction amount: ₹25.
* Electronics recorded the highest category sales at ₹156,905.
* Clothing recorded the highest quantity sold at 894 units.
* May 2023 recorded the highest monthly sales at ₹53,150.

## 8. Data Visualizations

The project includes five visualizations:

1. Total Sales by Product Category.
2. Sales Distribution by Gender.
3. Monthly Sales Trend.
4. Quantity Sold by Product Category.
5. Total Sales by Customer Age Group.

The chart images are stored in the `visualizations/` folder.

## 9. Power BI Dashboard

The Power BI dashboard presents retail sales performance through KPI cards, charts, a category summary, and filters.

The dashboard is designed to help users explore:

* Total sales.
* Total transactions.
* Total quantity sold.
* Sales by category.
* Sales by gender.
* Monthly sales trends.

The Power BI file should be included in the project or provided through an accessible sharing link.

## 10. Business Insights

1. Electronics generated the highest revenue among the three product categories.
2. Clothing recorded the highest quantity sold.
3. Female customers contributed approximately 51.1% of sales, while male customers contributed approximately 48.9%.
4. May 2023 had the highest monthly sales among the reported months.
5. September 2023 had the lowest monthly sales among the reported months of 2023.

## 11. Business Recommendations

1. Monitor electronics demand and maintain suitable stock levels for popular products.
2. Explore clothing promotions and product bundles to improve revenue.
3. Develop marketing campaigns that consider both male and female customers.
4. Investigate seasonal or operational factors that may explain monthly sales changes.
5. Verify whether January 2024 contains complete monthly data before comparing it with other months.

## 12. Conclusion

This project demonstrates how data analytics can turn retail transaction records into useful business information. The findings highlight category performance, customer sales distribution, and monthly trends. The Python analysis and Power BI dashboard provide a foundation for inventory planning, marketing decisions, and ongoing sales monitoring.
