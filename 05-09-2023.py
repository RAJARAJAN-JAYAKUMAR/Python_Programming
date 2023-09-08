# udf - user defined function
# functions - function is a block of code
# keyword - def

def add(a,b):
    c = a + b
    return c
a = 5
b = 7
print(add(a,b))
# you cannot add different datatypes in one. You should give apt datatypes that you specified in the udf

# insert values inside function
def sum(a,b):
    return a+b
print(sum(b = 'v',a = 'K'))

# giving default value
def color(a = 'black'):
    return 'I like you', a
print(color())
print(color('blue'))



