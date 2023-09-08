# '''
# function
# .user-defined 
# .built-in function such as print()

# keyword - def

# Types of argument
# required argument
# keyword argument
# default argument
# variable length argument  
# '''

# # return keyword only gives the output
def add(a,b);
    return a+b

print(add(1,2))


# # this above is keyword argument
def interest(p,t,r):
  return (p*t*r)/100
print(interest(t = 100, p = 1000, r = 2))

# # default argument
def simple(name, In = 'ITV') '''default values given in here'''
print(simple('raja')) 

# # variable length argument
def hi(*n) '''in here * is used to accept multiple argument at a time'''
    return n
n = range(10)
for j in n:
    print(hi(j))








