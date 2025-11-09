import pandas as pd
import sqlite3

df = pd.read_csv("sales_data.csv")
category_summary = df.groupby('Category').agg(
    total_quantity=('Quantity', 'sum'),
    average_price=('Price', 'mean'),
    max_quantity=('Quantity', 'max')
)
top_products = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_selling = top_products.loc[top_products.groupby('Category')['Quantity'].idxmax()]
df['TotalSales'] = df['Quantity'] * df['Price']
sales_by_date = df.groupby('Date')['TotalSales'].sum()
max_sales_date = sales_by_date.idxmax()

orders = pd.read_csv("customer_orders.csv")
orders_per_customer = orders.groupby('CustomerID')['OrderID'].count().reset_index(name='order_count')
active_customers = orders_per_customer[orders_per_customer['order_count'] >= 20]
avg_price_per_customer = orders.groupby('CustomerID')['Price'].mean().reset_index(name='avg_price')
high_spenders = avg_price_per_customer[avg_price_per_customer['avg_price'] > 120]
product_summary = orders.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', 'sum')
).reset_index()
filtered_products = product_summary[product_summary['total_quantity'] >= 5]

conn = sqlite3.connect("population.db")
population = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()
salary_bands = pd.read_excel("population salary analysis.xlsx")
population['SalaryCategory'] = pd.cut(
    population['Salary'],
    bins=salary_bands[['MinSalary', 'MaxSalary']].to_numpy().ravel(),
    labels=salary_bands['Category'],
    include_lowest=True
)
salary_stats = population.groupby('SalaryCategory').agg(
    population_percentage=('SalaryCategory', lambda x: len(x) / len(population) * 100),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median'),
    count=('Salary', 'count')
).reset_index()
state_salary_stats = population.groupby(['State', 'SalaryCategory']).agg(
    population_percentage=('SalaryCategory', lambda x: len(x) / len(population) * 100),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median'),
    count=('Salary', 'count')
).reset_index()
