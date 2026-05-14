import sys
print(sys.executable)
import os
print(os.getcwd())
# 1. Import libraries
import pandas as pd
# 2. Load dataset
df1= pd.read_csv("diabetes1.csv")
df2 = pd.read_csv("diabetes2.csv")
# 3. Show data
print("First data set:")
print(df1.head())
print("\n Second data set:")
print(df2.head())

print(df1.info())
print(df2.info())
print(df1.describe())
print(df2.describe())

# Function to calculate missing values and impute
def handle_missing(df):
    # 1. Calculate missing percentages
    missing_percent = df.isnull().mean() * 100
    print("Missing Values (%):\n", missing_percent)
    
    # 2. Impute missing values
    if 'Age' in df.columns:
        df['Age'].fillna(df['Age'].median(), inplace=True)
    if 'BMI' in df.columns:
        df['BMI'].fillna(df['BMI'].median(), inplace=True)
    if 'SmokingStatus' in df.columns:
        df['SmokingStatus'].fillna(df['SmokingStatus'].mode()[0], inplace=True)
    
    return df

# Apply to both datasets
df1 = handle_missing(df1)
df2 = handle_missing(df2)




