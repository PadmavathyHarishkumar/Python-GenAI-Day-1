Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#---------------------------------------Functions 2--------------------------------------------------

#Types of Arguments in user defined function:-
#1.)Default Arguments
#2.)Positional Arguments
#3.)Keyword Arguments
#4.)Arbitary Arguments

def mobile(brand,model,price):
    print(f'mobile brand is {brand} model is {model} price is {price}')

    
mobile('IQOO','NEO10',43000)
mobile brand is IQOO model is NEO10 price is 43000

#This is how a normal arugument works

#Default Arguments:-

def mobile(brand='realme',model='X2PRO',price=32000):
    print(f'mobile brand is {brand} model is {model} price is {price}')

    
mobile()
mobile brand is realme model is X2PRO price is 32000

#Here we have two advantages we can simply call the function and get the output as the arguments are already given inside the function and we can also change the arguments of the functions while calling the function to get a differnt output

mobile('redmi','note 4',15000)
mobile brand is redmi model is note 4 price is 15000

#Positional Arguments:-

def mobile(brand='realme',model='X2PRO',price=32000):
    print(f'mobile brand is {brand} model is {model} price is {price}')

    
mobile()
mobile brand is realme model is X2PRO price is 32000

#In the above function we exactly know the position of the parameters and passed the arguments
    
#What if we have 20 parameters we cant remember all postions of parameters

def mobile(brand='realme',model='X2PRO',price=32000):
    print(f'mobile brand is {brand} model is {model} price is {price}')

    
mobile('X2PRO','32000','realme')
mobile brand is X2PRO model is 32000 price is realme

#Here i forgot the position of the parameter and passed the arguments it has given the output but the output was not meaningful

#Now i want to change only brand and model

def mobile(brand='realme',model='X2PRO',price=32000):
    print(f'mobile brand is {brand} model is {model} price is {price}')

    
mobile('OPPO','F27')
mobile brand is OPPO model is F27 price is 32000

#Here i changed only brand and model but the price automatically came from function

#Now i want to change model and price

def mobile(brand='realme',model='X2PRO',price=32000):
    print(f'mobile brand is {brand} model is {model} price is {price}')

    
mobile('F31','30800')
mobile brand is F31 model is 30800 price is 32000

#Here the output was not meaningful so to overcome this keyword arguments has been introduced

#Keyword Arguments:-

def mobile(brand='realme',model='X2PRO',price=32000):
    print(f'mobile brand is {brand} model is {model} price is {price}')

    
mobile()
mobile brand is realme model is X2PRO price is 32000

#Now here i want to change model and price

mobile(price=30800,model='F31')
mobile brand is realme model is F31 price is 30800

#Here price is third parameter and model is second parameter but i interchanged the positions but the result came as expected so we can come to a conclusion that we dont have to remember the position of the parameters as we have seen in positional arguments

#Arbitary Arguments:-(Broadcast message)

def greet(*students):
    for i in students:
        print(f'hi {i} today there is no session on account of independance day')

        
greet('santhosh','padma','rishi','avinash','rishi','anuragh','syed','jennie','swathi','bharath','prakash','thuvarakesh')
hi santhosh today there is no session on account of independance day
hi padma today there is no session on account of independance day
hi rishi today there is no session on account of independance day
hi avinash today there is no session on account of independance day
hi rishi today there is no session on account of independance day
hi anuragh today there is no session on account of independance day
hi syed today there is no session on account of independance day
hi jennie today there is no session on account of independance day
hi swathi today there is no session on account of independance day
hi bharath today there is no session on account of independance day
hi prakash today there is no session on account of independance day
hi thuvarakesh today there is no session on account of independance day

def greet(*students):
    for i in students:
        print(f'hi {i} Happy independance day')

        
greet('santhosh','padma','rishi','avinash','rishi','anuragh','syed','jennie','swathi','bharath','prakash','thuvarakesh')
hi santhosh Happy independance day
hi padma Happy independance day
hi rishi Happy independance day
hi avinash Happy independance day
hi rishi Happy independance day
hi anuragh Happy independance day
hi syed Happy independance day
hi jennie Happy independance day
hi swathi Happy independance day
hi bharath Happy independance day
hi prakash Happy independance day
hi thuvarakesh Happy independance day

#Builtin Functions:-
#It is represented in purple colour
#Also known as Readymade function/Steady state function/Shipped function

import builtins
dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

#Above all are builtin functions
#The mostly used functions are:-
#1.)abs
abs(-12)
12

#Gives the absolute value

#2.)bin
bin(15)
'0b1111'

#Decimal to binary conversion

#3.)
#3.)bool
bool(0)
False
bool(1)
True
bool(-8)
True

#Gives boolean value

#4.)divmod
divmod(10,3)
(3, 1)

#Gives both quotient and remainder

#5.)chr
chr(A)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    chr(A)
NameError: name 'A' is not defined
chr('A')
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    chr('A')
TypeError: 'str' object cannot be interpreted as an integer
chr(65)
'A'
chr(97)
'a'

#Gives ascii values

#enumerate
for i in (harish):
    print(i)

    
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    for i in (harish):
NameError: name 'harish' is not defined. Did you mean: 'hash'?
for i in ('harish'):
    print(i)

    
h
a
r
i
s
h
for i in enumerate ('harish'):
    print(i)

    
(0, 'h')
(1, 'a')
(2, 'r')
(3, 'i')
(4, 's')
(5, 'h')

#Used to find the index

#7.)eval
eval('10+20')
30

#Evaluate mathematical expression eventhough its given inside ' '

#8.)len

name='harish'
len(name)
6

#gives the length of the string

#9.)min

min(20,30,10)
10

#Gives min value

#10.)
max(20,40,10)
40

#Gives max value

#11.)reversed

name='harish'
reversed(name)
<reversed object at 0x0000020B88231C90>
for i in reversed(name):
    print(i)

    
h
s
i
r
a
h
>>> 
>>> #12.)sorted
>>> sorted('harish')
['a', 'h', 'h', 'i', 'r', 's']
>>> sorted('harish')[::-1]
['s', 'r', 'i', 'h', 'h', 'a']
>>> 
>>> #Sorts array in ascending order
>>> 
>>> #13.)pow
>>> pow(14,3)
2744
>>> 
>>> #Does power calculation
>>> 
>>> #14.)sum
>>> sum([10,20,30,40])
100
>>> 
>>> #Gives the sum
>>> 
>>> #15.)round
>>> round(1.7)
2
>>> round(1.3)
1
round(2.7)
3
round(3.5)
4
round(4.5)
4

#Gives the round value
