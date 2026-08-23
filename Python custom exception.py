declared_value = 100
class NewError(Exception):
    '''class for new custom error'''
    pass

class MinimumValueError(NewError):
    '''raised when runtime value is lesser than declared value'''
    pass

class MaximumValueError(NewError):
    '''raised when runtime value is greater than declared value'''
    pass

runtime_value = int(input('Enter a numerical value:'))

try:
    if runtime_value < declared_value:
        raise MinimumValueError
    elif runtime_value > declared_value:
        raise MaximumValueError
    elif runtime_value == declared_value:
        print('Both values are same')
        exit()
except MinimumValueError as m:
    print(f'runtime value {runtime_value} is lesser than declared value {declared_value}')
except MaximumValueError as n:
    print(f'runtime value {runtime_value} is greater than declared value {declared_value}')
finally:
    print('*************************************')
