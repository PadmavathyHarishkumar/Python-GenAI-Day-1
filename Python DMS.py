Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Decision making statements(DMS)
#It is also called as conditional statement
#Most used conditional statements are
#1.)if
#2.)else
#3.)elif
#4.)nested if

#if
#if the given condition is satisfied then it prints something
#if the condition fails it prints nothing

name='harish'
if name=='harish':
    print('name is matched')

    
name is matched

#else   
#if the given condition is true then it runs if block statement   
#else it will run else block statement

gold_price=120000
if gold_price>=120000:
    print('gold price was high')
else:
    print('gold price was low')

    
gold price was high

gold_price=110000

if gold_price>=120000:
    print('gold price was high')
else:
    print('gold price was low')

    
gold price was low

#elif
#elif is used to check multiple conditions for a single value

temp=103
if (temp>= 99) && if (temp<=100):
    
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
if temp>=99 and temp<=100:
    print('low fever')
... elif temp>100 and temp<=102:
...     print('mild fever')
... elif temp>102 and temp<=104:
...     print('high fever')
... elif temp>104 and temp<=106:
...     print('very high fever')
... else:
...     print('normal just need some sleep')
... 
...     
high fever
>>> 
>>> temp=97
>>> temp
97
>>> if temp>=99 and temp<=100:
...     print('low fever')
... elif temp>100 and temp<=102:
...     print('mild fever')
... elif temp>102 and temp<=104:
...     print('high fever')
... elif temp>104 and temp<=106:
...     print('very high fever')
... else:
...     print('normal just need some sleep')
... 
...     
normal just need some sleep

#nested if
#It has one test condition inside another test condition
#If the outer block condition fails i will run else block

age = 18
voteid ='available'
if age>=18:
    print('eligible for vote')
if voteid == 'available':
    
SyntaxError: invalid syntax
age = 18
voteid ='available'
if age>=18:
    print('eligible for vote')
    
SyntaxError: multiple statements found while compiling a single statement
age =18
voteid ='available'
if age>=18:
    print('eligible for voting')
    if voteid == 'available':
        print('you can vote')
    else:
        print('apply for voteid')
else:
    print('Not eligible to vote')

    
eligible for voting
you can vote

age =18
voteid ='Not available'
if age>=18:
    print('eligible for voting')
    if voteid == 'available':
        print('you can vote')
    else:
        print('apply for voteid')
else:
    print('Not eligible to vote')
    
SyntaxError: multiple statements found while compiling a single statement

age = 18
voteid='Not available'
if age>=18:
    print('eligible for voting')
    if voteid == 'available':
        print('you can vote')
    else:
        print('apply for voteid')
else:
    print('Not eligible to vote')

    
eligible for voting
apply for voteid

age=17
voteid='Not available'
if age>=18:
    print('eligible for voting')
    if voteid == 'available':
        print('you can vote')
    else:
        print('apply for voteid')
else:
    print('Not eligible to vote')

    
Not eligible to vote
