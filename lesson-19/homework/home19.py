
import pandas as pd

# Загрузка данных
sales_df = pd.read_csv("task/sales_data.csv")


category_stats = sales_df.groupby("Category").agg(
    total_quantity_sold=("Quantity", "sum"),
    avg_price=("Price", "mean"),
    max_quantity_single_transaction=("Quantity", "max")
)
print("1. Category Aggregates:\n", category_stats)

и
top_products = sales_df.groupby(["Category", "Product"])['Quantity'].sum().reset_index()
top_per_category = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False]).groupby('Category').first()
print("\n2. Top-selling product per category:\n", top_per_category)

sales_df['TotalSales'] = sales_df['Quantity'] * sales_df['Price']
total_sales_per_date = sales_df.groupby("Date")['TotalSales'].sum()
max_sales_date = total_sales_per_date.idxmax()
print("\n3. Date with highest total sales:", max_sales_date)

orders_df = pd.read_csv("task/customer_orders.csv")


order_counts = orders_df.groupby('CustomerID')['OrderID'].nunique()
active_customers = order_counts[order_counts >= 20].index
filtered_customers_df = orders_df[orders_df['CustomerID'].isin(active_customers)]
print("1. Customers with 20+ orders:\n", filtered_customers_df)


avg_price_per_customer = orders_df.groupby("CustomerID")["Price"].mean()
high_value_customers = avg_price_per_customer[avg_price_per_customer > 120].index
print("\n2. Customers with avg price > $120:\n", high_value_customers)

product_summary = orders_df.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", "sum")
)
filtered_products = product_summary[product_summary["total_quantity"] >= 5]
print("\n3. Product summary with quantity >= 5:\n", filtered_products)


import sqlite3
import numpy as np


salary_bands_df = pd.read_excel("task/population salary analysis.xlsx")


bands = []
for _, row in salary_bands_df.iterrows():
    lower = row['LowerBound']
    upper = row['UpperBound']
    name = row['Category']
    bands.append((lower, upper, name))


conn = sqlite3.connect("task/population.db")
population_df = pd.read_sql("SELECT * FROM population", conn)


def get_salary_band(salary):
    for lower, upper, name in bands:
        if lower <= salary < upper:
            return name
    return "Other"

population_df['SalaryBand'] = population_df['Salary'].apply(get_salary_band)


salary_band_stats = population_df.groupby('SalaryBand').agg(
    count=('Salary', 'count'),
    avg_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
)
total_population = len(population_df)
salary_band_stats['percentage'] = (salary_band_stats['count'] / total_population) * 100
print("2. Salary Band Statistics:\n", salary_band_stats)

state_band_stats = population_df.groupby(['State', 'SalaryBand']).agg(
    count=('Salary', 'count'),
    avg_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
)

state_totals = population_df.groupby('State').size()
state_band_stats['percentage'] = state_band_stats.apply(
    lambda row: (row['count'] / state_totals[row.name[0]]) * 100, axis=1
)
print("\n3. State-wise Salary Band Statistics:\n", state_band_stats)
