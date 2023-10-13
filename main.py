# there should be an __init__ method in every package we create cause it tell python, its a package

# from shopping_package.module1 import * | # use * to import all things in the file
from shopping.module1 import *
from shopping.more_shopping.shopping_cart import buy

# print(module1)
# print(shopping_cart)
print(addition(1,2))
print(buy("laptop"))


print(__name__) # result is __main__ cause these import the other modules in these file. if you rename it it show, __main__ only
if __name__ == '__main__':
  print('The file name') # to rename it use this if clause but it wont work on other files than main


class Student():
  pass
st1 = Student()
print(st1) #result = <__main__.Student object at 0x0000026E211D2ED0> in console

print(st2) #result = <shopping.module1.Student object at 0x00000216A62A7690> in console




