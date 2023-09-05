a = {'raja', 'Rajan'}
print(a)
# print(a[1]) It doesnt support indexing
# To add single element use add method
a.add('yellow')
print(a)
# To add multiple element in set use update method
a.update('is', 'my', 'colour')
print(a)

a = {1,2,3,4,5}
b = {2,3,4,5,6}


print(a&b) # common values
print(a|b) # return all unique values
print(b-a) # return difference of values
print(a^b) # return values other than common

#exercise

a = {'java', 'Python', 'C++'}
for i in a:
    print('i have completed', i)

a = [1,2,3,4,5]
b = 0
for i in a:
   c = b + i
   b = c
print(c)

a = [1,2,3,4,5]
b = 1
for i in a:
   c = b * i
   b = c
print(c)

# a = [3,5,2,4,1]
# a.sort()
# print(max(a))
# print(min(a))

# a = [3,1,2]
# for i in a:
#     for j in range(len(a)):
#       if i < a[j]:
#         z = [i]
#         print(z, end=",")
#

def bub(q):
    n = len(q)
    for i in range(n):
        sw = False
        for j in range(0,n-i-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                sw = True
        if not sw:
            break
    print('the smallest number is', )

q = [1,4,2,4,23,3]
bub(q)
print(q)



a = 'Rajarajan'

b = 'aannanaa'
print(b.strip('a'))
print(b.lstrip('a'))
print(b.rstrip('a'))
print(a.count('a',0, 4))

# dictionary
a={1: "Raja", '2':'rajan'}
print(a)
print(a['2'])
a['2'] ='Rajann'
print(a)
print(a.keys())
print(a.values())
print(a.items())
b = {3: 'good boy'}
a.update(b)
print(a)




