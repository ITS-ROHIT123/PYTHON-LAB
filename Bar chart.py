"""1.Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 

Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 

# Monthly expenses in dollars (replace with your own data) 

expenses = [1200, 400, 200, 150, 250]"""

import matplotlib.pyplot as plt

# Categories and expenses data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Monthly Expenses by Category')
plt.xlabel('Spending Categories')
plt.ylabel('Expenses ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()

# Conclusion based on the data
total_expenses = sum(expenses)
most_expensive_category = categories[expenses.index(max(expenses))]
most_expensive_amount = max(expenses)

conclusion = (
    f"Total Monthly Expenses: ${total_expenses}\n"
    f"The most expensive category is {most_expensive_category} with ${most_expensive_amount} in expenses."
)
print(conclusion)
