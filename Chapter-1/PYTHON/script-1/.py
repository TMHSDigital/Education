import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# Replace 'data.csv' with the path to your dataset
data = pd.read_csv('data.csv')

# Display first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Basic Data Analysis
print("\nBasic Statistics:")
print(data.describe())

print("\nData Types:")
print(data.dtypes)

# Visualization
# Histogram of a numerical column
plt.figure(figsize=(10, 6))
data['column_name'].hist(bins=30)
plt.title('Distribution of Column Name')
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.show()

# Scatter plot between two numerical columns
plt.figure(figsize=(10, 6))
plt.scatter(data['column1'], data['column2'])
plt.title('Scatter Plot of Column1 vs Column2')
plt.xlabel('Column1')
plt.ylabel('Column2')
plt.show()

# Bar plot of a categorical column
plt.figure(figsize=(10, 6))
data['categorical_column'].value_counts().plot(kind='bar')
plt.title('Bar Plot of Categorical Column')
plt.xlabel('Categories')
plt.ylabel('Frequency')
plt.show()

# Save plots as images
plt.figure(figsize=(10, 6))
data['column_name'].hist(bins=30)
plt.title('Distribution of Column Name')
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.savefig('histogram.png')

plt.figure(figsize=(10, 6))
plt.scatter(data['column1'], data['column2'])
plt.title('Scatter Plot of Column1 vs Column2')
plt.xlabel('Column1')
plt.ylabel('Column2')
plt.savefig('scatter_plot.png')

plt.figure(figsize=(10, 6))
data['categorical_column'].value_counts().plot(kind='bar')
plt.title('Bar Plot of Categorical Column')
plt.xlabel('Categories')
plt.ylabel('Frequency')
plt.savefig('bar_plot.png')
