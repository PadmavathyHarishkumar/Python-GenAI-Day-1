Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Set
>>> #1.Set is enclosed with {}
>>> #2.Set is unordered collection of data
>>> #3.Set is unindexed
>>> #4.Set doesn't support duplicate values
>>> #5.Popping is allowed from start to end
>>> 
>>> brand='samsung'
>>> brand
'samsung'
>>> type(brand)
<class 'str'>
>>> brand={samsung}
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    brand={samsung}
NameError: name 'samsung' is not defined
>>> brand={'samsung'}
>>> brand
{'samsung'}
>>> type(brand)
<class 'set'>
>>> 
>>> #Here first point is verified set is enclosed with{}
>>> 
>>> electronics={'haier','whirlpool','bosch','samsung','lg','lg'}
electronics
{'whirlpool', 'bosch', 'samsung', 'lg', 'haier'}

#Points two, three and four was proved here

mobiles={'samsung','lg','apple','vivo','nokia'}
mobiles
{'samsung', 'lg', 'apple', 'vivo', 'nokia'}

electronics.add('gordrej')
electronics
{'whirlpool', 'bosch', 'samsung', 'lg', 'gordrej', 'haier'}
mobiles
{'samsung', 'lg', 'apple', 'vivo', 'nokia'}
electronics.discard('gordrej')
electonics
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    electonics
NameError: name 'electonics' is not defined. Did you mean: 'electronics'?
electronics
{'whirlpool', 'bosch', 'samsung', 'lg', 'haier'}

#add function adds a value to an random index
#discard deletes a particular value

electronics.difference(mobile)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    electronics.difference(mobile)
NameError: name 'mobile' is not defined. Did you mean: 'mobiles'?
electronics.difference(mobiles)
{'whirlpool', 'haier', 'bosch'}

#difference function is used to remove the common values between two sets

electronics
{'whirlpool', 'bosch', 'samsung', 'lg', 'haier'}
electronics.difference_update()
electronics
{'whirlpool', 'bosch', 'samsung', 'lg', 'haier'}
electronics.difference_update(b)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    electronics.difference_update(b)
NameError: name 'b' is not defined
electronics.difference_update(mobiles)
electronics
{'whirlpool', 'bosch', 'haier'}
mobiles
{'samsung', 'lg', 'apple', 'vivo', 'nokia'}

#difference update will update the current updated value permanently

electronics.add('samsung')
electronics.add('lg')
electronics
{'whirlpool', 'bosch', 'lg', 'samsung', 'haier'}
mobiles
{'samsung', 'lg', 'apple', 'vivo', 'nokia'}
electronics.isdisjoint(mobiles)
False

#disjoint function ensures that there are no common values between two sets here electonics and mobiles has two common values so it returned false

electronics.issubset(mobiles)
False

electronics.issuperset(mobiles)
False

electronics.union(mobiles)
{'whirlpool', 'lg', 'haier', 'vivo', 'nokia', 'bosch', 'samsung', 'apple'}

#union will concatenate both sets without duplicates

electronics.pop()
'whirlpool'
electronics.pop()
'bosch'

#Here fifth point is also proved that pop happens from start to end

electronics
{'lg', 'samsung', 'haier'}

electronics.remove('haier')
electronics
{'lg', 'samsung'}

electronics.issubset(mobiles)
True
mobiles.issuperset(electronics)
True

electronics
{'lg', 'samsung'}
mobiles
{'samsung', 'lg', 'apple', 'vivo', 'nokia'}

electronics.add('whirlpool')
electronics.aadd('haier')
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    electronics.aadd('haier')
AttributeError: 'set' object has no attribute 'aadd'. Did you mean: 'add'?
electronics.add('haier')
electronics.add('bosch')
electronics
{'bosch', 'haier', 'whirlpool', 'lg', 'samsung'}
mobiles
{'samsung', 'lg', 'apple', 'vivo', 'nokia'}
electronics.intersection(mobiles)
{'samsung', 'lg'}

#intersection function will return the common values between both sets

electronics
{'bosch', 'haier', 'whirlpool', 'lg', 'samsung'}
mobiles
{'samsung', 'lg', 'apple', 'vivo', 'nokia'}

electronics.symmetric_difference(mobiles)
{'bosch', 'whirlpool', 'apple', 'haier', 'vivo', 'nokia'}

#symmetric difference is the opposite of intersection it will not return common values

electronics.update(mobiles)
electronics
{'whirlpool', 'lg', 'haier', 'vivo', 'nokia', 'bosch', 'samsung', 'apple'}
mobiles
{'samsung', 'lg', 'apple', 'vivo', 'nokia'}
