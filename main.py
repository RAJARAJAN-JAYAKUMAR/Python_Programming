

import math
a=(10,20)
print(math.ceil(5.4))
print(math.floor(5.4))
print(math.pow(5,5))
print(math.exp(4))
print(math.sqrt(6))
print(math.fabs(-5))
print(len(a))
print(max(12,3,4,5,6,4))
# list indexing
_list = list(range(20))
tup = _list
print(_list)
print(_list[0])
# slicing
print(_list[1:3])
print(_list[1:20:10])
# reverse
print(_list[20:1:-10])
# repeatation
print(_list*2)
# concat
b = [0,0,0,0]
print(_list+b)
# length
print(len(_list))
# append
_list.append(50)
print(_list)
# insert
_list.insert(2,100)
print(_list)
# extend
c = [900,000,8]
_list.extend(c)
print(_list)
# adding list inside list
_list.insert(3,c)
print(_list)
# pop to remove the last element and return the value
print(_list.pop(0))
# remove
print(_list.remove(3))
# clear
print(_list.clear())
tup = list(range(20))

print(tuple(tup))

# strings manipulation
a = 'Raja_is_a_good_boy_8'
print(min(a))
print(max(a))
print(a[1:3])
print(a[::-1])
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.isspace())
print(a.islower())
print(a.upper())
print(a.lower())
print(a.title())
b = a.capitalize()
print(b)
print(a.swapcase())