import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load Dataset
df = pd.read_csv("student_placement_synthetic.csv")

# Preview Dataset
print(df.head())

# Dataset Information
print(df.info())

# Missing Values
print(df.isnull().sum())

# Placement Distribution
print(df['placement_status'].value_counts())

sns.countplot(x='placement_status', data=df)
plt.title("Placement Distribution")
plt.show()

# CGPA vs Placement
sns.boxplot(x='placement_status', y='cgpa', data=df)
plt.title("CGPA vs Placement")
plt.show()

# Internship vs Placement
sns.boxplot(x='placement_status', y='internships', data=df)
plt.title("Internships vs Placement")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12,8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm'
)

plt.title("Feature Correlation Heatmap")

plt.show()

# Drop Salary Column
df = df.drop('salary_package_lpa', axis=1)

# Final Null Check
print(df.isnull().sum())