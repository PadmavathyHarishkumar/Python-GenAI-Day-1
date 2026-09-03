import pandas as pd
import numpy as np
print('Taking a txt file and converting to DataFrame')
print('='*40)
data=pd.read_csv('Patterns using file handling.txt')
print(f'{data}\n')

print('Converting DataFrame to csv')
print('='*40)
data.to_csv('Patterns using file handling.csv', index=False)
with open('Patterns using file handling.csv','r')as file:
    print(file.read())

print('Taking a txt file and converting to DataFrame')
print('='*40)
data=pd.read_csv('Patterns using file handling.txt')
print(f'{data}\n')

print('Converting DataFrame to excel')
print('='*40)
data.to_excel('Patterns using file handling.xlsx', index=False)
data_excel = pd.read_excel('Patterns using file handling.xlsx')
print(data_excel)

