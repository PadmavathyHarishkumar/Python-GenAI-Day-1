Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Identifiers

name = 'harish'
age = 29

name
'harish'
age
29

#Types of Identifiers
#Private identifier
_name = 'harish'

#Strong private identifier
__name = 'harish'

#Magical method identifier
__name__ ='harish'

#Literals

type(name)
<class 'str'>
type(age)
<class 'int'>

#Literals are used to find the data types of the given identifiers

#Operators

#Arithmetic operator(+ - * / % //)
a=10
b=20

a+b
30

a-b
-10

a*b
200

a/b
0.5

a//b
0

#// will do integer division

a%b
10
>>> #% will give remainder
>>> 
>>> #Logical operator(AND OR NOT)
>>> a=30
>>> b=20
>>> 
>>> a==30 & b==20
False
>>> 
>>> (a==30)&(b==20)
True
>>> 
>>> # AND operator if both conditions are true then the output is true
>>> 
>>> #OR operator
>>> 
>>> (a==30)|(b==10)
True
>>> 
>>> #OR operator if any one condition is true then the output is true
>>> 
>>> #Relational Operator(> >= < <= == !=)
>>> 
>>> a=30
>>> b=20
>>> 
>>> a>b
True

a>=b
True

a<b
False

a<=b
False

a==b
False

a!=b
True

#Relational operator compares two variables so it is also called comparision operator

# Assignment operator
# Assignment operator(+= -= *= /= %= //=)

a=30
a+=30
(a+=30)
SyntaxError: invalid syntax
a += 30
a
90

a-=30
a
60

a*=3
a
180

a/=3
a
60.0

a//=3
a
20.0
a=int(a)
a
20
a%=4
a
0

#Unlike other operators assignment operator keeps on upgrading

#Membership operator(in not in)
name = 'harish'
name
'harish'
'h' in name
True

'h' not in name
False
False
False
#Membership operator is used to find whether the given character is available or not
#Mostly used in contact book , ticket booking app , amazon product stock availablity
#Mostly used in contact book , ticket booking app , amazon product stock availablity

#Identity operator(is is not)
a=30
a
30
a==30
True
a is 30
True

a is not 30
False

#Keywords
help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

#Where are these keywords used

#Looping statement
for and while
SyntaxError: invalid syntax
for/while
SyntaxError: invalid syntax
'Decision making statement:-
SyntaxError: unterminated string literal (detected at line 1)
  if/else/elif'
  
SyntaxError: unexpected indent

#Flow control statement(break continue pass)

#User defined statement(def/return/yield)

#OOPS statement(class/del)

#Boolean(true/false)

#Exception handling(try/except/finally)

#Modules programming(import/from/as)

#operators(and/or/not/is/in)

#file handling(while)

