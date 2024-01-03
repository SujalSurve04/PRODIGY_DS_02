# PRODIGY_DS_02
# Task Two - Data Cleaning and Exploratory Data Analysis (EDA)

## Description
This repository contains the code for Task Two, which involves data cleaning and exploratory data analysis (EDA) on a given dataset.

## Dataset
The dataset used for this task is named `Datasettask1.csv`. It includes the following columns:
- Name
- Age
- Email
- Phone
- Address

## Prerequisites
Make sure you have the following libraries installed:
- pandas
- numpy
- seaborn
- matplotlib

You can install them using the following command:
```bash
pip install pandas numpy seaborn matplotlib
Instructions
Clone this repository to your local machine.
Ensure you have Python installed.
Install the required libraries using the command mentioned above.
Run the Task2.py script using the following command:
bash
Copy code
python Task2.py
Tasks Accomplished
Loaded the dataset and displayed basic information.
Checked for missing values in the dataset.
Performed data cleaning:
Converted the 'Age' column to numeric, replacing non-numeric values with NaN.
Imputed missing values in 'Age' with the mean.
Replaced 'Missing Address' in 'Address' with NaN.
Forward-filled missing values in 'Address'.
Replaced missing values in 'Name' with 'Unknown'.
Conducted Exploratory Data Analysis (EDA):
Explored the distribution of 'Age'.
Explored the distribution of 'Phone' lengths.
Explored relationships between variables (e.g., 'Age' vs. 'Phone_Length').
Explored the distribution of email domains.
Explored the distribution of ages by gender.
Explored the most common names.
Author
Sujal Surve
