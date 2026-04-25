import pandas as pd

df = pd.read_csv("placement_data.csv")

# Check data
print(df.head())

# Handle missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Convert placed column
df['placed'] = df['placed'].map({'Yes':1, 'No':0})

print(df.info())


# Placement rate
placement_rate = df['placed'].mean() * 100
print("Placement Rate:", placement_rate)

# Avg salary
avg_salary = df[df['placed']==1]['salary'].mean()
print("Average Salary:", avg_salary)

# CGPA vs Placement
print(df.groupby('placed')['cgpa'].mean())

# Internships impact
print(df.groupby('internships')['placed'].mean())


import matplotlib.pyplot as plt

# CGPA vs Salary
plt.scatter(df['cgpa'], df['salary'])
plt.xlabel("CGPA")
plt.ylabel("Salary")
plt.title("CGPA vs Salary")
plt.show()

# Placement count
df['placed'].value_counts().plot(kind='bar')
plt.title("Placement Count")
plt.show()