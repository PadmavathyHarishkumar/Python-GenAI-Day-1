Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List
>>> #1.List is always enclosed in []
>>> #2.List contains ordered collection of data items
>>> #3.List is mutable and changeable
>>> #4.List can contain duplicate values
>>> #5.List values are indexed
>>> #6.List contains hetrogenous values
>>> 
>>> tree=['mango','apple','banyan','coconut','neem']
>>> tree
['mango', 'apple', 'banyan', 'coconut', 'neem']
>>> type(tree)
<class 'list'>
>>> #The first two points of list was covered in above two lines, enclosed in [] and contains ordered collection of data items what order the user given as input the same order will come as processed output
>>> 
>>> tree=['mango','apple','banyan','banyan','neem']
>>> tree
['mango', 'apple', 'banyan', 'banyan', 'neem']
>>> #fourth point is also verified that List can contain duplicate values
>>> 
>>> tree=['I have',1,'mango tree',2,'apple tree']
>>> tree
['I have', 1, 'mango tree', 2, 'apple tree']
>>> ['I have', 1, 'mango tree', 2, 'apple tree']
['I have', 1, 'mango tree', 2, 'apple tree']
#here the sixth point is also verified that it can contain heterogeneous values that means we can have Int,String,Float or any datatype inside one list

tree=['mango','apple','banyan','banyan','neem']
tree
['mango', 'apple', 'banyan', 'banyan', 'neem']

#Now lets look at some set of dotted functions for list

tree.index(1)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tree.index(1)
ValueError: 1 is not in list
tree=['mango','apple','banyan','banyan','neem']
tree
['mango', 'apple', 'banyan', 'banyan', 'neem']
tree.index('apple')
1
tree.index('banyan')
2
tree[1]
'apple'
tree[2]
'banyan'

#Here the fifth point is verified that values of and list are indexed

#what if user wants values from certain indexes

tree[2:4]
['banyan', 'banyan']

tree[2:]
['banyan', 'banyan', 'neem']

tree[:2]
['mango', 'apple']

#These are indexing,Slicing,Ranging that we covered in string operations the same method we can use here in list also this is called as preprocessing

tree[4,'coconut']
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    tree[4,'coconut']
TypeError: list indices must be integers or slices, not tuple
tree[3]='coconut'
tree
['mango', 'apple', 'banyan', 'coconut', 'neem']

tree.append('chocolate')
tree
['mango', 'apple', 'banyan', 'coconut', 'neem', 'chocolate']

#append adds a new value on the end of the list

tree.clear()
tree
[]

#clear removes all of the values from the list

tree.append('mango')
tree.append('apple')
tree.append('banyan')
tree
['mango', 'apple', 'banyan']

tree.extend(['coconut','neem','chocolate'])
tree
['mango', 'apple', 'banyan', 'coconut', 'neem', 'chocolate']

#Extend is used to add values in single line whereas in append we have to create seperate lines for every value addition

tree.insert[2,'guava']
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    tree.insert[2,'guava']
TypeError: 'builtin_function_or_method' object is not subscriptable
tree.insert(2,'guava')
tree
['mango', 'apple', 'guava', 'banyan', 'coconut', 'neem', 'chocolate']

#insert is used to add a new value to the given index and move all the other indices to the right

tree.remove(3)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    tree.remove(3)
ValueError: list.remove(x): x not in list
tree.remove('banyan')
tree
['mango', 'apple', 'guava', 'coconut', 'neem', 'chocolate']

#remove is used to delete a value from the list

#Note in remove function we have to give the value for deletion giving index and empty() will throw an error

tree.pop()
'chocolate'
tree
['mango', 'apple', 'guava', 'coconut', 'neem']
tree.pop(2)
'guava'
tree
['mango', 'apple', 'coconut', 'neem']

#pop function is almost the reverse of remove function here we can give index and empty() for deletion but if we give the original value it will throw an error

#Note pop() will always delete the value from the end of the list

tree.reverse()
tree
['neem', 'coconut', 'apple', 'mango']

#reverse function reverses the entire list this is also came from string operations ::-1 reverses the entire string

tree(::-1)
SyntaxError: invalid syntax
tree[::-1]
['mango', 'apple', 'coconut', 'neem']

tree.count('coconut')
1
tree.count('neem')
1

#count function is used to find the frequency of values in the given list

dup_tree=tree
dup_tree
['neem', 'coconut', 'apple', 'mango']

dup_tree[2]='palm'
dup_tree
['neem', 'coconut', 'palm', 'mango']

tree
['neem', 'coconut', 'palm', 'mango']

#here we changed the value only on dup_tree list but it also affected the original list although it seems right it is not legally right and this type of copying is called shallow copy

dup_tree=tree.copy()
dup_tree
['neem', 'coconut', 'palm', 'mango']

dup_tree[2]='apple'
dup_tree
['neem', 'coconut', 'apple', 'mango']

tree
['neem', 'coconut', 'palm', 'mango']

#here the change on the dup_tree list didnt affect the original list because the copy function not only copied the original value but also the memory of the original list this type of copying is called deep copy

tree.sort()
tree
['coconut', 'mango', 'neem', 'palm']

#sort function arranges the list in ascending order
