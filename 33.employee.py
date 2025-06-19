import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)  # For reproducibility
num_employees = 10
names = [f"Employee{i+1}" for i in range(num_employees)]
salaries = np.random.randint(5000, 99001, size=num_employees)  # 5000 to 99000

# Create DataFrame
df = pd.DataFrame({
    'Name': names,
    'Salary': salaries
})

# Filter rows where salary > 50,000
high_salary_df = df[df['Salary'] > 50000]

# Output
print("All Employees:\n", df)
print("\nEmployees with Salary > 50,000:\n", high_salary_df)
