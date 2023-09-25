# Public
# Private
# Protected

# public
class employee:
    def fun1(self,a):
        self.a = a
        print('hello')
class second(employee):
    def fun2(self):
        print(self.a)
s=second()
s.fun1(10)
s.fun2()

# private
class employee:
    def fun1(self,a):
        self.__a = a
        print(self.__a)
class second(employee):
    def fun2(self):
        print(self.__a)

s=second()
s.fun1(10)
s.fun2()

# abstraction
import abc
from abc import ABC
class vehicle(ABC):
    def speed(self):
        pass
class car(vehicle):
    def speed(self):
        print('average speed is 80km/hr')
class bus(vehicles):
    def speed(self):
        print('average speed is 100km/hr')

s = vehicle()
print(s)

''' Exceptional handling
1.checked - code run panumpothu error katum , can be rectified
2.unchecked - codela mistake irukathu ana output show agathu. can be rectified, num divided by zero
3.error - rectify pannamudiyathu, storage full anuchuna output show agathu
unchecked- try block, except block, finally block

'''

try:
    a=10
    b=8
    print(a/b)
    
except:
    print('error occured')

try:
    a=10
    b=0
    print(a/b)
    
except:
    print('error occured')

try:
    a=[10,20,30]
    print(a[6])
    
except:
    print('list index out of range')


