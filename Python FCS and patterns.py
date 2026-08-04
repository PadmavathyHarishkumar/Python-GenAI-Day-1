Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Flow control statement(FCS) and Pattern printing:-
>>> 
>>> #Break:-
>>> #Break keyword is used to stop the flow of the code when an given condition is met
>>> 
>>> for i in range(11):
...     print(i,end=' ')
... 
...     
0 1 2 3 4 5 6 7 8 9 10 
>>> 
>>> for i in range(11):
...     if i==6:
...         break;
...     print(i,end=' ')
... 
...     
0 1 2 3 4 5 
>>> 
>>> #Here in the above lines of code break is before print so it printed till 5
>>> 
>>> #How to print till number 6?
>>> 
>>> for i in range(11):
...     print(i,end=' ')
...     if i==6;
    
SyntaxError: invalid syntax
for i in range(11):
    print(i,end=' ')
    if i==6:
        break

    
0 1 2 3 4 5 6 

#Now the code will print first and then break

#Continue:-
#Continue keyword is used to skip elements when certain condition is met and then resume from next element

for i in range(11):
    print(i,end=' ')
    if i==6:
        continue

    
0 1 2 3 4 5 6 7 8 9 10 

#As per the definition number 6 should have been skipped but 6 also printed in output this is because we are printing first and then skipping so it prints all numbers including 6
#How to print without 6:-

for i in range(11):
    if i==6:
        break
    print(i,end=' ')

    
0 1 2 3 4 5 
for i in range(11):
    if i==6:
        continue
    print(i,end=' ')

    
0 1 2 3 4 5 7 8 9 10 

#Now six is not there because it skips first and then prints

car=['corolla','civic','innova','fortuner','bolero','thar','defender','mustang']

#Print the name of the cars that has not exactly 7 characters

#Solution 1(without using FCS):-
for i in car:
    print(i)

    
corolla
civic
innova
fortuner
bolero
thar
defender
mustang

for i in car:
    print(i,len(i))

    
corolla 7
civic 5
innova 6
fortuner 8
bolero 6
thar 4
defender 8
mustang 7

for i in car:
    if len(i)!=7:
        print(i)

        
civic
innova
fortuner
bolero
thar
defender

#Solution 2(using FCS)

for i in car:
    if len(i)==7:
        continue
    print(i)

    
civic
innova
fortuner
bolero
thar
defender

#Pattern printing:-
#Print right angled triangle using integers

for i in range(1,6):
    for j in range(0,i):
        print(i,end=' ')
    print()

    
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

#Here i is the outer loop ---> prints row wise ---> and tells which number to print
#And  j is the inner loop ---> prints col wise ---> and tells how many times the number should print

#Col printing:

for i in range(1,6):
    for j in range(0,i):
        print(j,end=' ')
    print()

    
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 

#Star printing:
for i in range(1,6):
    for j in range(0,i):
        print(*,end=' ')
    print()
    
SyntaxError: Invalid star expression
#Star printing:
for i in range(1,6):
    for j in range(0,i):
        print('*',end=' ')
    print()

    
* 
* * 
* * * 
* * * * 
* * * * * 

#Character printing(uppercase and lowercase):

#Uppercase unicode string value printing

for i in range(1,6):
    for j in range(0,i):
        print(i+64,end=' ')
    print()

    
65 
66 66 
67 67 67 
68 68 68 68 
69 69 69 69 69 

#Uppercase unicode string value printing(col wise)

#Uppercase unicode string value printing

for i in range(1,6):
    for j in range(0,i):
        print(j+65,end=' ')
    print()

    
65 
65 66 
65 66 67 
65 66 67 68 
65 66 67 68 69 

#Uppercase character printing(row wise)

#Way 1:

#Uppercase unicode string value printing

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
A 
B B 
C C C 
D D D D 
E E E E E 

#Way 2:


for i in range(1,6):
    for j in range(0,i):
        print(i+96,end=' ')
    print()

    
97 
98 98 
99 99 99 
100 100 100 100 
101 101 101 101 101 

for i in range(1,6):
    for j in range(0,i):
        print(i+96,end=' ')
    print()

    
97 
98 98 
99 99 99 
100 100 100 100 
101 101 101 101 101 

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+96-32),end=' ')
    print()

    
A 
B B 
C C C 
D D D D 
E E E E E 

#Print uppercase col wise:

for i in range(1,6):
    for j in range(0,i):
        print(chr(j+65),end=' ')
    print()

    
A 
A B 
A B C 
A B C D 
A B C D E 

#Print lowercase row wise:

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+96),end=' ')
    print()

    
a 
b b 
c c c 
d d d d 
e e e e e 

#Print lowercase col wise:

for i in range(1,6):
    for j in range(0,i):
        print(chr(j+97),end=' ')
    print()

    
a 
a b 
a b c 
a b c d 
a b c d e 

#Printing inverse triangle:
#1.Row wise
#2.Col wise
#Star pattern
#Uppercase row wise
#Uppercase col wise
#Lowercase row wise
#Lowercase col wise

for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=' ')
    print()

    
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

for i in range(5,0,-1):
    for j in range(0,i):
        print(j,end=' ')
    print()

    
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1 
0 

for i in range(5,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print()

    
* * * * * 
* * * * 
* * * 
* * 
* 

for i in range(5,0,-1):
    for j in range(0,i):
        print(i+64,end=' ')
    print()

    
69 69 69 69 69 
68 68 68 68 
67 67 67 
66 66 
65 

for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
E E E E E 
D D D D 
C C C 
B B 
A 

for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(j+65),end=' ')
    print()

    
A B C D E 
A B C D 
A B C 
A B 
A 
for i in range(5,0,-1):
    for j in range(0,i):
        print(i+96,end=' ')
    print()

    
101 101 101 101 101 
100 100 100 100 
99 99 99 
98 98 
97 

for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(i+96),end=' ')
    print()

    
e e e e e 
d d d d 
c c c 
b b 
a 
for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(j+97),end=' ')
    print()

    
a b c d e 
a b c d 
a b c 
a b 
a 
