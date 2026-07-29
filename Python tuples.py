Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Tuple
>>> #1.Tuple is always enclosed with()
... #2.Tuple contains ordered collection of data items
... #3.Tuple is IMMUTABLE
... #4.Tuple can contain duplicate values
... #5.Tuple values are indexed
... #6.Tuple contains hetrogenous values
>>> 
>>> #Tuples are almost the same as list but the only difference is tuples are IMMUTABLE
>>> 
>>> mobile='samsung'
>>> mobile
'samsung'
>>> type(mobile)
<class 'str'>
>>> 
>>> mobile=('samsung','realme','realme','redmi')
>>> mobile
('samsung', 'realme', 'realme', 'redmi')
>>> type(mobile)
<class 'tuple'>
>>> 
>>> #The points one, two, and four are verified here
>>> 
>>> #Tuple functions
>>> 
mobile.count('samsung')
1
mobile.count('realme')
2

#The count function came from list and works exactly the same

mobile.index('redmi')
3
mobile.index('realme')
1

#This also came from list her the fifth point was also verified

#Note tuple only has two dotted fuctions(count, index) what can we do if we want to add extra values

#There are two ways to do it
#1.Typecasting
#2.tuple concatenation

#Typecasting
mobile=list(mobile)
mobile
['samsung', 'realme', 'realme', 'redmi']
mobile.append('vivo')
mobile
['samsung', 'realme', 'realme', 'redmi', 'vivo']
mobile.insert[2,'oppo']
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    mobile.insert[2,'oppo']
TypeError: 'builtin_function_or_method' object is not subscriptable
mobile.insert(2,'oppo')
mobile
['samsung', 'realme', 'oppo', 'realme', 'redmi', 'vivo']

mobile=tuple(mobile)
mobile
('samsung', 'realme', 'oppo', 'realme', 'redmi', 'vivo')

#TUPLE CONCATENATION
mobile_price=(10000,15000,25000)
mobile_price
(10000, 15000, 25000)
mobile=mobile+mobile_price
mobile
('samsung', 'realme', 'oppo', 'realme', 'redmi', 'vivo', 10000, 15000, 25000)

