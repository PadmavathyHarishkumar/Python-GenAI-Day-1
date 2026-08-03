Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Looping statements(for/while)
#For loop:-
#Iterating through the given set of elements n-1 times until the given test condition satisfies
#We dont have to give incremental value seperately on for loop

for i in range(5):
    print(i)

    
0
1
2
3
4
for i in range(0,5):
    print(i)

    
0
1
2
3
4
for i in range(0,5,1):
    print(i)

    
0
1
2
3
4

#In above lines of code (i) is the name of the item (0) is the starting point (5) is the stopping point (1) is the incremental operator but as said above incremental is not required in for loop

#How to print horizontally:-
for i in range(11):
    print(i,end=' ')

    
0 1 2 3 4 5 6 7 8 9 10 

#Print all the even numbers:-
#How to print horizontally:-
for i in range(11):
    if i%2==0:
        print(i)

        
0
2
4
6
8
10

#Optimised approach:-
#How to print horizontally:-
for i in range(0,11,2):
    print(i,end=' ')

    
0 2 4 6 8 10 

#Print odd numbers:-


for i in range(1,11,2):
    print(i,end=' ')

    
1 3 5 7 9 

names=['harish','padma','dev','shakthi','dharan','anu','sumathi','devi']
names
SyntaxError: multiple statements found while compiling a single statement

names=['harish','padma','dev','shakthi','dharan','anu','sumathi','devi']
names
['harish', 'padma', 'dev', 'shakthi', 'dharan', 'anu', 'sumathi', 'devi']
#Print names that starts with letter s

for i in names:
    print(i)

    
harish
padma
dev
shakthi
dharan
anu
sumathi
devi

for i in names:
    if i.startswith('s'):
        print(i)

        
shakthi
sumathi

#Print names that ends with letter (i)

for i in names:
    if i.endswith('i'):
        print(i)

        
shakthi
sumathi
devi

#Print names that have more than 4 characters:-

for i in names:
    if len(i)>=5:
        print(i)

        
harish
padma
shakthi
dharan
sumathi

#Print names that have vowels as their ending character

for i in names:
    if i.endswith(('a','e','i','o','u')):
        print(i)

        
padma
shakthi
anu
sumathi
devi

#Using nested for:-

vowels=['a','e','i','o','u']
for i in names:
    for j in vowels:
        if i.endswith(j):
            print(i)

            
padma
shakthi
anu
sumathi
devi

#Print numbers in reverse:-

for i in range(10,0,-1)
SyntaxError: expected ':'
for i in range(10,0,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
for i in range(10,0,-1):
    print(i,end=' ')

    
10 9 8 7 6 5 4 3 2 1 

#While loop:-
#While loop is exactly same as for loop it will run through each element to check whether the given condtion is true or not
#But in while loop incremental value is mandatory
#If we did'nt give incremental or decremental value then the loop will run infinite times

a=5
while a>0:
    print(a,end=' ')
    a-=1

    
5 4 3 2 1 

a=0
while a<6:
    print(a,end=' ')
    a+=1
... 
...     
0 1 2 3 4 5 
>>> 
>>> #Printing odd and even numbers using while loop:-
>>> 
>>> a=0
>>> while a<11:
...     if a%2==0:
...         print(a,' - even')
...     else:
...         print(a,' - odd')
...     a+=1
... 
...     
0  - even
1  - odd
2  - even
3  - odd
4  - even
5  - odd
6  - even
7  - odd
8  - even
9  - odd
10  - even
>>> 
