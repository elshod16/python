
import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)




df=df.rename(columns={'First name':'first_name','Age':'age'})
df
df.head(3)


mean_age = df['age'].mean()
print("Mean age:", mean_age)

df[['First Name','age']]

import random

df['Salary'] = [random.randint(4000, 8000) for _ in range(len(df))]
print(df)


df.describe()


import pandas as pd

# 1. Jadval yaratish
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

# 2. Maksimum qiymatlar
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

# 3. Minimum qiymatlar
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

# 4. O‘rtacha qiymatlar
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

# Natijalarni chiqarish
print(sales_and_expenses)
print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)
print("Minimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)
print("Average Sales:", avg_sales)
print("Average Expenses:", avg_expenses)



import pandas as pd

# 1. DataFrame yaratish
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# 2. Category ustunini index sifatida o‘rnatish
expenses = expenses.set_index('Category')

# 3. Har bir kategoriya bo‘yicha maksimal, minimal va o‘rtacha qiymatlarni hisoblash
max_expense = expenses.max(axis=1)
min_expense = expenses.min(axis=1)
avg_expense = expenses.mean(axis=1)

# 4. Natijalarni chiqarish
print("Expenses DataFrame:")
print(expenses)
print("\nMaximum expense for each category:")
print(max_expense)
print("\nMinimum expense for each category:")
print(min_expense)
print("\nAverage expense for each category:")
print(avg_expense)
