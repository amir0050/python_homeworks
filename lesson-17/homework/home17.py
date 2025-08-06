
import pandas as pd
import numpy as np

# Исходные данные
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)


df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

print("First 3 rows:\n", df.head(3))


mean_age = df['age'].mean()
print("\nMean age:", mean_age)

print("\nSelected columns:\n", df[['first_name', 'city']])


df['salary'] = np.random.randint(4000, 10000, size=len(df))
print("\nWith salary column:\n", df)


print("\nSummary statistics:\n", df.describe())


sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})


print("\nMax Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())


print("\nMin Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())


print("\nAverage Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())


expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})


expenses = expenses.set_index('Category')


print("\nMax expense per category:\n", expenses.max(axis=1))

print("\nMin expense per category:\n", expenses.min(axis=1))


print("\nAverage expense per category:\n", expenses.mean(axis=1))
