Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Exception Handling:
#Two important things in exception handling:
#1.Error
#2.Exception

#Error:
#It is a misbehaved part of a program
#It is a unintentional mistake done which stops the program execution
#The program will never run without correcting the errors

#Exception:
#It is an unwanted or an unexpected event which disrupts the normal execution flow of the program abnormally
#Exception always looks for an alternate code

#Now lets see some of the builtin errors:
#1.Value error
int(input('Enter a value:'))
Enter a value:harish
Traceback (most recent call last):
  File "<pyshell#0>", line 17, in <module>
    int(input('Enter a value:'))
ValueError: invalid literal for int() with base 10: 'harish'

#2.Type error
34+'34'
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    34+'34'
TypeError: unsupported operand type(s) for +: 'int' and 'str'

#3.Assertion error
assert(3+3==10)
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    assert(3+3==10)
AssertionError

#4.Zerodivision error
5/0
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    5/0
ZeroDivisionError: division by zero

#How many builtin errors are there?
import builtins
dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

#Error vs Exception
#Error                                                    Exception
#-------------------------------------------------------------------
#Error cant be identified        |       Exception can be identified
#Error cant be tolerated         |       Exception can be tolerated
#Error cant be corrected         |       Exception can be corrected
#Error cant be followed          |       Exception can be followed
#Error cant be controlled        |       Exception can be controlled

#Two most commonly seen errors:
#1.Syntax error(Developer responsible error)
#2.Runtime error(Both developer and user responsible error)

#Reasons:
#When inappropriate values are given
#When inadequate values are given
#When program logic is uneven

#Exception handling keywords:
#1.try
#2.except
#3.finally

#try and except:
try:
    5/0
except:
    print('Enter a valid input')

    
Enter a valid input

try:
    5/2
except:
    print('Enter a valid input')

    
2.5

#Note:
... #The expect block will only execute when the try block fails
... #We can create many except blocks in a same code but try block should be created only once
... 
... #finally:
... try:
...     5/0
... except:
...     print('Enter a valid input')
... finally:
...     print('------------- END ------------')
... 
...     
Enter a valid input
------------- END ------------
>>> 
>>> try:
...     5/0
... finally:
...     print('------------- END ------------')
... 
...     
------------- END ------------
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    5/0
ZeroDivisionError: division by zero

