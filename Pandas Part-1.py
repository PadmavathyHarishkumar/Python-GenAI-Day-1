#1.Pandas(Panel Data Structure(not official))
#------------------------------------------
#Pandas is a python library built for handling and analyzing structured data

#Uses of pandas:
#---------------
#Data processing
#Data cleaning
#Data retrieving
#Data Monitoring
#Data Handling
#Data Replacement

#Data structures of pandas:
#--------------------------
#Series(1Dimensional)
#DataFrame(2Dimensional)
#Panel
#Panel 4D

#Note:
#-----
#In pandas outcome should be on 73% accuracy and more or else it will not be satisfied

import pandas as pd
import numpy as np
#2.Understanding Series:
#-----------------------
#A series is like a single column in excel it is a list of values with labels(called index)

#Note:
#In pandas we have to give index value manually or else it will take default values like(0,1,2,3) as index

#Creating a series of fruits from a list:
#----------------------------------------
fruits=pd.Series(['Apple','Mango','Grapes','Orange'])
print('1.Series of fruits without manual indexing:')
print('='*40)
print('Series of fruits:')
print(f'{fruits}\n')

fruits=pd.Series([100,50,30,40],('Apple','Mango','Grapes','Orange'))
print('2.Series of fruits with manual indexing:')
print('='*40)
print(f'{fruits}\n')

print('3.Index of fruits:')
print('='*40)
print(f'{pd.Index(fruits)}\n')

#Examples with duplicate values
print('4.Manual indexing with duplicate values without using dictionary:')
print('='*40)
car=pd.Series(['virtus','creta','santafe','passat','polo'],index = ['vw','hyundai','hyundai','vw','vw'])
print(f'{car}\n')

print('5.Printing using index values:')
print('='*40)
print(f'{car}\n')
print('After printing using index values')
print('='*40)
print(f'{car['vw']}\n')

print('6.Manual indexing with duplicate keys using dictionary:')
print('='*40)
car=pd.Series({'vw':'virtus','hyundai':'creta','hyundai':'santafe'})
print(f'{car}\n')

#Dictionary does'nt allow duplicate keys

print('7.Manual indexing with duplicate values using dictionary:')
print('='*40)
car=pd.Series({'vw':'virtus','honda':'creta','hyundai':'creta'})
print(f'{car}\n')

#Dictionary duplicate values are allowed

#3.Understanding DataFrame:
#----------
#DataFrame is like a excel spreadsheet with rows and columns
data ={'name':['harish','padma','dev','venkhat','kumar'],'age':[29,25,20,31,68],'salary':[32000,40000,50000,60000,70000],'dept':['IT','HR','IT','Finance','HR']}
df=pd.DataFrame(data)
print('8.Employee Data')
print('='*40)
print(f'{df}\n')

#Printing size of the table using shape function:
#------------------------------------------------
print('9.Size of the table')
print('='*40)
print(f'{df}\n')
print(f'shape:{df.shape}\n')

#Printing type of the table using type function:
#------------------------------------------------
print('10.Type of the Data')
print('='*40)
print(f'{type(df)}\n')

#4.Useful methods to explore data:
#-------------------------------
#Head()function:
#---------------
#Used to get the required data from top to bottom using index values
print('11.Printing using HEAD function')
print('='*40)
print(f'{df}\n')
print('Result of printing using head()function')
print('='*40)
print(f'{df.head(3)}\n')

#Tail()function:
#---------------
#Used to get the required data from bottom to top using index values
print('12.Printing using TAIL function')
print('='*40)
print(f'{df}\n')
print('Result of printing using tail()function')
print('='*40)
print(f'{df.tail(3)}\n')

#Note:-In head() and tail()function only ranging is possible slicing is not possible

#Describe()function:
#-------------------
#Used to get count/average/min/max/standard deviation of the data
print('13.Printing using DESCRIBE function')
print('='*40)
print(f'{df}\n')
print('Result of printing using describe()function')
print('='*40)
print(f'{df.describe()}\n')

#5.Accessing Data from DataFrame:
#--------------------------------
print('14.Taking a random colum and printing the required index')
print('='*40)
print(f'{df}\n')
print(f'{df.columns}\n')
print('After printing required columns the result will be')
print('='*40)
print(f'{(df['name'][:2])}\n')

#Accessing Multiple columns:
#---------------------------
print('15.Printing multiple columns')
print('='*40)
print(f'{df}\n')
print('Result of printing multiple columns')
print('='*40)
print(f'{df[['name','salary']]}\n')

#.loc[]function:
#---------------
#Accessed by label(user specified index)
#Used to filter by using labels
print('16.Slicing list using loc function')
print('='*40)
print('Way 1 with label values:')
print(f'{df}\n')
print('After slicing the list will be')
print('='*40)
print(f'{(df.loc[2:4,['name','salary']])}\n')

print('Way 2 without label values')
print(f'{df}\n')
print('After slicing the list will be')
print('='*40)
print(f'{(df.loc[2:4])}\n')

#iloc[]function:
#---------------
#Accessed by position(String indexing)
#Used to filter by using index
print('17.Slicing list using iloc function')
print('='*40)
print(f'{df}\n')
print('After slicing the list will be')
print('='*40)
print(f'{(df.iloc[2:4])}\n')

#6.Filtering Data:
#-----------------
print('18.Filtering data by using column labels')
print('='*40)
print('Way 1 using single condition:')
print(f'{df}\n')
print('After filtering the list will be')
print('='*40)
print(f'{(df[df['salary']>=50000])}\n')

print('Way 2 using multiple condition:')
print(f'{df}\n')
print('After filtering the list will be')
print('='*40)
print(f'{df[(df['salary']>=30000) & (df['dept']=='IT')]}\n')

#7.Sorting Data:
#---------------
print('19.Sorting data by age(youngest to oldest) labels')
print('='*40)
print('Way 1 using single condition:')
print(f'{df}\n')
print('After sorting the list will be')
print('='*40)
print(f'{(df.sort_values('age'))}\n')

print('20.Sorting data by age(oldest to youngest) labels')
print('='*40)
print(f'{df}\n')
print('After sorting the list will be')
print('='*40)
print(f'{(df.sort_values('age',ascending = False))}\n')

print('Way 2 using multiple condition:')
print(f'{df}\n')
print('After filtering the list will be')
print('='*40)
print(f'{(df.sort_values(['dept','salary'],ascending = [False,False]))}\n')

#8.Basic calculations and statistics:
#------------------------------------
#Statistics calculation
print('21.Calculating statistics of age')
print('='*40)
print(f'{df}\n')
print(f'Average of age:{df['age'].mean():.2f}')
print(f'Median of age:{df['age'].median()}')
print(f'Minimum age:{df['age'].min()}')
print(f'Maximum age:{df['age'].max()}')
print(f'Standard deviation of age:{df['age'].std():.2f}')
print(f'Sum of age:{df['age'].sum()}\n')

#Adding a new column
print('22.Adding a new column using calculations')
print('='*40)
print(f'{df}\n')
df['salary dollar'] = df['salary']/96
print('After adding salary dollar column')
print('='*40)
print(f'{df[['name','salary','salary dollar']]}\n')

#Creating a new conditional column:
print('23.Adding a new conditional column based on department')
print('='*40)
print('Way 1 using user defined function')
df=pd.DataFrame(data)
print(f'{df}\n')
def calculate_bonus(dept):
    if(dept == 'IT'):
        return 7000
    elif(dept == 'Finance'):
        return 5000
    else:
        return 3000
df['bonus'] = df['dept'].apply(calculate_bonus)
print('After adding new bonus column using user defined function')
print('='*40)
print(f'{df[['name','salary','dept','bonus']]}\n')

print('Way 2 using lambda function')
df=pd.DataFrame(data)
print(f'{df}\n')
df['bonus'] = df.apply(lambda row : 7000 if row['dept']=='IT' else(5000 if row['dept']=='Finance' else 3000),axis=1)
print('24.After adding new bonus column using lambda function')
print('='*40)
print(f'{df[['name','salary','dept','bonus']]}\n')

#9.Grouping and Aggregation:
#---------------------------
#Finding average salary of department
print('25.Printing average salary by department')
print('='*40)
print(f'{df}\n')
dept_avg_salary = df.groupby('dept')['salary'].mean()
print('After calculating average salary by department')
print('='*40)
print(f'{dept_avg_salary}\n')

#Finding size of the department
print('26.Number of employees per department is')
print('='*40)
dept_count = df.groupby('dept').size()
print(f'{dept_count}\n')

#Multiple aggregations at once:
print('27.Printing using multiple aggregations')
print('='*40)
print(f'{df}\n')
print('Result after using multiple aggregations on salary')
print('='*40)
dept_stats = df.groupby('dept')['salary'].agg(['mean','min','max','count'])
print(f'{dept_stats}\n')

#10.Handling missing data:
#------------------------
#Creating a data frame with missing values
messy_data = {'name':['harish','padma','dev','venkhat','kumar'],'age':[29,np.nan,20,31,68],'salary':[32000,40000,np.nan,60000,70000],'dept':['IT','HR','IT',np.nan,'HR']}
df_messy = pd.DataFrame(messy_data)
print('28.Creating a table with missing values')
print('='*40)
print(f'{df}\n')
print('After creating a table with missing values')
print('='*40)
print(f'{df_messy}\n')

#Count of missing values
print('29.Count of missing values')
print('='*40)
print(f'{df_messy.isnull().sum()}\n')

#Rows with null values
print('30.Finding rows with null values')
print('='*40)
row_null = df_messy.isnull().any(axis=1)
print(f'{df_messy.loc[row_null]}\n')

#Columns with null values
print('31.Finding columns with null values')
print('='*40)
col_null = df_messy.isnull().any(axis=0)
print(f'{df_messy.loc[:,col_null]}\n')

#Rows without null values
print('32.Finding rows without null values')
print('='*40)
row_not_null = df_messy.notnull().all(axis=1)
print(f'{df_messy.loc[row_not_null]}\n')

#Columns without null values
print('33.Finding columns without null values')
print('='*40)
col_not_null = df_messy.notnull().all(axis=0)
print(f'{df_messy.loc[:,col_not_null]}\n')

#Size after removing rows with missing values
print('34.Original size of messy data ')
print('='*40)
print(f'{df_messy.shape}\n')
print('After cleaning row wise the size will be')
df_clean = df_messy.dropna()
print(f'{df_clean.shape}\n')

#Size after removing columns with missing values
print('35.Original size of messy data ')
print('='*40)
print(f'{df_messy.shape}\n')
print('After cleaning column wise the size will be')
df_clean = df_messy.dropna(axis=1)
print(f'{df_clean.shape}\n')

#Filling missing values with constants
print('36.Filling missing value with constants')
print('='*40)
print(f'{df_messy}\n')
print('After filling with constants the data will look like')
print('='*40)
df_clean1 = df_messy.copy()
df_clean1.fillna({'age':df_clean1['age'].mean(),'salary':0,'dept':'--'},inplace = True)
print(f'{df_clean1}\n')

#Filling missing values using ffill
print('37.Filling missing value with ffill')
print('='*40)
print(f'{df_messy}')
print('\nAfter filling with ffill the data will look like')
print('='*40)
df_clean2 = df_messy.copy()
df_clean2.ffill(inplace=True)
print(f'{df_clean2}\n')

#Filling missing values using bfill
print('38.Filling missing value with bfill')
print('='*40)
print(f'{df_messy}')
print('\nAfter filling with bfill the data will look like')
print('='*40)
df_clean2 = df_messy.copy()
df_clean2.bfill(inplace=True)
print(f'{df_clean2}\n')
