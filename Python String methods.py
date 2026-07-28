Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''String operations
... 1.Indexing
... 2.Slicing
... 3.Ranging '''
'String operations\n1.Indexing\n2.Slicing\n3.Ranging '
>>> 
>>> #Indexing
>>> name = 'harish'
>>> name[0]
'h'
>>> name[4]
's'
>>> name[6]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name[6]
IndexError: string index out of range
>>> 
>>> #Indexing will start from zero not one
>>> 
>>> name[5]
'h'
>>> 
>>> #Slicing
>>> name = 'harish kumar'
>>> name
'harish kumar'
name[1:6]
'arish'
name[7:11]
'kuma'

#Slicing is used to get a particular set of characters even from middle of the given string

#Ranging
name= 'harish kumar'
name[:6]
'harish'
name[6:]
' kumar'
name[:10]
'harish kum'

# Ranging will return the whole given range as processed output
#Here we are giving only Starting range or Stopping range so it will not act as slicing both of them does the same operation but this is the difference between them

#String Methods
#1.Concatenation
#2.Repetition
#3.Formatting

#Concatenation

name = 'harish'
age = '29'
city = 'Chennai'
age =(int)age
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
age=int(age)
name
'harish'
age
29
city
'Chennai'
name+city
'harishChennai'
name+age
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name+age
TypeError: can only concatenate str (not "int") to str
name+str(age)
'harish29'

#Concatenation is used to add two or more strings
#Used in form filling for E.g we fill first name and last name in seperate blocks in form but when we view the form after filling they will be in the same line her concatenation is used

#Repetition
name='harish'
name
'harish'
name*5
'harishharishharishharishharish'

name= 'kumar'
name
'kumar'
name*4
'kumarkumarkumarkumar'

#Repetition will not add it will multiply the values of the container
#Used in online delivery platforms adding multiple pieces of same product

#Formatting
#1.Manual formatting
#2.Automated formatting
#3.General formatting
#4Formatted String (fstring)

#Manual formatting
name= 'harish'
age= 29
city= 'chennai'

print('my name is [0] aged [1] from [3]'.format(name,age,city))
my name is [0] aged [1] from [3]
print('my name is{0} aged {1} from {3}'.format(name,age,city))
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print('my name is{0} aged {1} from {3}'.format(name,age,city))
IndexError: Replacement index 3 out of range for positional args tuple
print('my name is{0} aged{1} from{2}'.format(name,age,city))
my name isharish aged29 fromchennai

#Automated formatting
name= 'harish'
age= '29'
city- 'chennai'
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    city- 'chennai'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
city= 'chennai'
name
'harish'
age
'29'
city
'chennai'
print('my name is %s from %s aged %s'%(name,city,age))
my name is harish from chennai aged 29

#General formatting

name = 'harish'
age = 29
city = 'Chennai'

print('my name is',name 'iam from',city 'aged',age)
SyntaxError: invalid syntax
print('my name is',name,'iam from',city,'aged',age)
my name is harish iam from Chennai aged 29

#Formatted String
name='harish'
age='29'
city='chennai'

print(f'my name is {name} from {city} aged {age}')
my name is harish from chennai aged 29

#String supporting functions(Dedicated string methods)
name='harish'
name
'harish'
name.capitalize
<built-in method capitalize of str object at 0x000002095A4941E0>
name.capitalize()
'Harish'
name.casefold()
'harish'
name='harish'
name='HArish'
name
'HArish'
name.casefold()
'harish'
#Casefold converts all uppercase letter to lowercase letter

name.find(h)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    name.find(h)
NameError: name 'h' is not defined
name.find('h')
5
name.find('H')
0
name='harish'
name.find('h')
0
name.find('z')
-1
#Find is used to find the index of a particular character

name.index('h')
0
name.index('r')
2
name.index('z')
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    name.index('z')
ValueError: substring not found
#Note here index does not return -1 instead it shows error and this is because find will look for the character but index will surely say the character is in the string if it is not there it will throw an error

name.center(50)
'                      harish                      '
name.ljust(50)
'harish                                            '
name.rjust(50)
'                                            harish'

#Center,ljust,rjust is used to align the data

name.zfill(10)
'0000harish'
name.zfill(10,'*')
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    name.zfill(10,'*')
TypeError: str.zfill() takes exactly one argument (2 given)
name.center(10,'*')
'**harish**'
num=130
num.center(10,'*')
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    num.center(10,'*')
AttributeError: 'int' object has no attribute 'center'
name='130'
name.center(10,'*')
'***130****'

name.ljust(10,'*')
'130*******'
name.rjust(10,'*')
'*******130'

name='harish'
name
'harish'
name.strip()
'harish'
'harish'
'harish'
name='harish kumar'
name.strip()
'harish kumar'
name='**harish**kumar'
name
'**harish**kumar'
name.strip()
'**harish**kumar'
name='harish kumar'
name
'harish kumar'
name.lstrip()
'harish kumar'
name.lstrip(50)
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    name.lstrip(50)
TypeError: lstrip arg must be None or str
name='     harish    '
name
'     harish    '
name.strip()
'harish'

name.lstrip()
'harish    '
name.rstrip()
'     harish'
#Strip is used to clear all the white spaces

name='HarishKumar'
name
'HarishKumar'
name.split()
['HarishKumar']
name='harish kumar'
name.split()
['harish', 'kumar']
#split will seperate a single string into two or more strings based on the number of spaces

name.isalnum()
False
name.isalpha()
False
name='harish'
name
'harish'
name.isalpha()
True
name.isascii()
True
name.isdecimal()
False

name.count('h')
2
name.endswith('r')
False
name.startswith('a')
False

#count is used to find the frequency of characters in given string

name='harish kumar'
name
'harish kumar'
name.isspace()
False
#isspace doesnt ask whether there is a space in the string it asks whether the whole string is a space
name='       '
name.isspace()
True
name.isasii()
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    name.isasii()
AttributeError: 'str' object has no attribute 'isasii'. Did you mean: 'isascii'?
name.isascii()
True
#Space also has an ascii value which is 32

name='harish'
name
'harish'
name.strip('h')
'aris'
name.lstrip('h')
'arish'
name.rstrip('h')
'haris'
name.join('123')
'1harish2harish3'
name.isidentifier()
True
name.islower()
True
name.isupper()
False
name.partition()
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    name.partition()
TypeError: str.partition() takes exactly one argument (0 given)
name='harish kumar;
SyntaxError: unterminated string literal (detected at line 1)
name='harish kumar'
name
'harish kumar'
name.partition()
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    name.partition()
TypeError: str.partition() takes exactly one argument (0 given)
name.partition('')
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    name.partition('')
ValueError: empty separator
name = 'harish kumar'
name
'harish kumar'
name.partition(' ')
('harish', ' ', 'kumar')
name.partition('h')
('', 'h', 'arish kumar')
('', 'h', 'arish kumar')
('', 'h', 'arish kumar')
name.partition('har')
('', 'har', 'ish kumar')
name.removeprefix()
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    name.removeprefix()
TypeError: str.removeprefix() takes exactly one argument (0 given)
name.removeprefix('h')
'arish kumar'
name.removesuffix('h')
'harish kumar'
name.removesuffix('r')
'harish kuma'
name.removeprefix('har')
'ish kumar'
'-'.join('09','06','1997')
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    '-'.join('09','06','1997')
TypeError: str.join() takes exactly one argument (3 given)
'-'.join(['09','06','1997'])
'09-06-1997'
name.title()
'Harish Kumar'
name.title()
'Harish Kumar'
name.replace('h','*')
'*aris* kumar'
