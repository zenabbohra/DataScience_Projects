
import pandas as pd
import matplotlib as plt
import numpy as np
from scipy.stats import mode

df = pd.read_csv("train_data.csv")


# Find out mode in a column
print mode(df['Loan_Amount_Term']).mode[0]


# Input mode in place of missing valaue
df['Gender'].fillna(mode(df['Gender']).mode[0], inplace = True)
df['Dependents'].fillna(mode(df['Dependents']).mode[0], inplace = True)
df['Self_Employed'].fillna(mode(df['Self_Employed']).mode[0], inplace = True)
df['Credit_History'].fillna(mode(df['Credit_History']).mode[0], inplace = True)
df['Married'].fillna(mode(df['Married']).mode[0], inplace = True)
df['LoanAmount'].fillna(mode(df['LoanAmount']).mode[0], inplace = True)
df['Loan_Amount_Term'].fillna(mode(df['Loan_Amount_Term']).mode[0], inplace = True)

def count_missing_value(x):
  return sum(x.isnull())
# print df.apply(count_missing_value, axis = 0)


print df.describe()