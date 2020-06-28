# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
#print(bank_data.shape)
#print(bank_data.dtypes)

#Categorical columns
categorical_var = bank_data.select_dtypes(include='object')
print(categorical_var)

#Numerical columns
numerical_var = bank_data.select_dtypes(include='number')
print(numerical_var)

#dropping Loan_ID column
banks = bank_data.drop('Loan_ID', axis=1)

#missing values in each column
print(banks.isnull().sum())

#estimating mode(repeating value)
bank_mode = banks.mode()

#replacing the missing values with mode
for i in banks.columns:
    banks[i].fillna(bank_mode[i][0], inplace=True)
print(banks.isnull().sum().values.sum())

#pivot table categorizing the required columns based on the loan amount (mean)
avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount')

#loan approved status based on self employment
loan_approved_se = len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]) 
loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])

#total loan status
Loan_Status = len(banks)

#percentage of loan approved based on self employement
percentage_se = loan_approved_se/Loan_Status*100
percentage_nse = loan_approved_nse/Loan_Status*100

#converting loan term from months to year
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term = len(loan_term[loan_term>=25])

#grouping based on applicant income and credit history 
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()








