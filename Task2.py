# Importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the dataset
df = pd.read_csv('Datasettask2.csv')

# Display basic information about the dataset
print(df.info())

# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Data Cleaning

# Convert 'Age' column to numeric, replacing non-numeric values with NaN
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Impute missing values in 'Age' with the mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Replace 'Missing Address' in 'Address' with NaN
df['Address'].replace('Missing Address', np.nan, inplace=True)

# Forward fill missing values in 'Address'

df['Address'].fillna(method='ffill', inplace=True)

# Replace missing values in 'Name' with 'Unknown'
df['Name'].fillna('Unknown', inplace=True)

# Confirm that there are no missing values anymore
print("Missing values after cleaning:")
print(df.isnull().sum())

# Exploratory Data Analysis (EDA)

# Explore the distribution of 'Age'
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Distribution of Age')
plt.show()

# Explore the distribution of 'Phone' lengths
df['Phone_Length'] = df['Phone'].apply(lambda x: len(str(x)) if pd.notna(x) else 0)
sns.countplot(x='Phone_Length', data=df)
plt.title('Distribution of Phone Lengths')
plt.show()

# Explore relationships between variables (e.g., 'Age' vs. 'Phone_Length')
sns.scatterplot(x='Age', y='Phone_Length', data=df)
plt.title('Relationship between Age and Phone Length')
plt.xlabel('Age')
plt.ylabel('Phone Length')
plt.show()

# Explore the distribution of email domains
df['Email_Domain'] = df['Email'].str.split('@').str[1]
plt.figure(figsize=(10, 6))
sns.countplot(y='Email_Domain', data=df, order=df['Email_Domain'].value_counts().index[:10])
plt.title('Top 10 Email Domains')
plt.xlabel('Count')
plt.show()

# Explore the distribution of ages by gender
df['Gender'] = df['Name'].apply(lambda x: 'Male' if 'Mr.' in x else ('Female' if 'Mrs.' in x else 'Unknown'))

# Plotting the distribution of ages by gender
plt.figure(figsize=(8, 5))
sns.histplot(x='Age', hue='Gender', data=df, bins=20, kde=True)
plt.title('Distribution of Ages by Gender')
plt.xlabel('Age')
plt.show()

# Explore the most common names
df['First_Name'] = df['Name'].apply(lambda x: x.split()[0])
plt.figure(figsize=(10, 6))
sns.countplot(y='First_Name', data=df, order=df['First_Name'].value_counts().index[:10])
plt.title('Top 10 Most Common Names')
plt.xlabel('Count')
plt.show()

# Remove additional columns used for analysis
df.drop(['Phone_Length', 'Email_Domain', 'Gender', 'First_Name'], axis=1, inplace=True)
