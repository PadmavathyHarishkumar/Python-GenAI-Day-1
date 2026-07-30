Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Dictionary
>>> #1.Dictionary is enclosed with{}
>>> #2.Dictionary follows(key:values)as paired items instead of indexing
>>> #3.Dictionary does not support duplicates
>>> #4.Popping happens form end
>>> 
>>> brand='samsung'
>>> brand
'samsung'
>>> type(brand)
<class 'str'>
>>> 
>>> AC={'brand':'lg','type':'split','capacity':1.5,'price':48000}
>>> AC
{'brand': 'lg', 'type': 'split', 'capacity': 1.5, 'price': 48000}
>>> 
>>> type(AC)
<class 'dict'>
>>> 
>>> AC={'brand':'lg','type':'split','capacity':1.5,'price':48000,'price':49000}
>>> AC
{'brand': 'lg', 'type': 'split', 'capacity': 1.5, 'price': 49000}
>>> 
>>> #Here the first three points are verified but here it just didn't remove the duplicate but it upadated new key and new value
>>> 
AC
{'brand': 'lg', 'type': 'split', 'capacity': 1.5, 'price': 49000}
AC.pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    AC.pop()
TypeError: pop expected at least 1 argument, got 0

#An empty pop will throw an error so we need to give a key that we need to remove

AC.pop('brand')
'lg'
AC
{'type': 'split', 'capacity': 1.5, 'price': 49000}

AC.popitem()
('price', 49000)
AC
{'type': 'split', 'capacity': 1.5}

#popitem function will remove the last (key:value) pair and here fourth point is also verified

AC
{'type': 'split', 'capacity': 1.5}

AC.clear()
AC
{}

#clear function deletes every (key:value) pair

AC={'brand':'lg','type':'split','capacity':1.5,'price':48000}
AC
{'brand': 'lg', 'type': 'split', 'capacity': 1.5, 'price': 48000}
AC.keys()
dict_keys(['brand', 'type', 'capacity', 'price'])

#Keys function will return the list of keys in dictionary

AC
{'brand': 'lg', 'type': 'split', 'capacity': 1.5, 'price': 48000}

AC.values()
dict_values(['lg', 'split', 1.5, 48000])

#Values function will return list of values from dictionary

AC.items()
dict_items([('brand', 'lg'), ('type', 'split'), ('capacity', 1.5), ('price', 48000)])

#Items function will return the list of both key and value pairs in the format of list of tuples

AC.get('brand')
'lg'

#Get function is used to get a value from a key

AC
{'brand': 'lg', 'type': 'split', 'capacity': 1.5, 'price': 48000}
AC.fromkeys()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    AC.fromkeys()
TypeError: fromkeys expected at least 1 argument, got 0
AC.fromkeys('type')
{'t': None, 'y': None, 'p': None, 'e': None}

AC.fromkeys("brands","types","ton","MRP")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    AC.fromkeys("brands","types","ton","MRP")
TypeError: fromkeys expected at most 2 arguments, got 4

AC.fromkeys(('brands','types','ton','MRP'))
{'brands': None, 'types': None, 'ton': None, 'MRP': None}
{'brands': None, 'types': None, 'ton': None, 'MRP': None}
{'brands': None, 'types': None, 'ton': None, 'MRP': None}

#from keys function is used to create a new dictionary with default values
