def oddoreven(x):
    l1=[]
    l2=[]
    for i in x:
        if i%2==0:
            l1.append(i)
        else:
            l2.append(i)
    print(l1, l2)
    return
x = [1,2,3,4,5,6,7,8,9,10]
print(oddoreven(x))

# fibonnaci series
def fuc(n):
    if n<=1:
        return n
    else:
        return(fuc(n-1) + fuc(n-2))
n = 10
if n<0:
    print('negative number')
else:
    for i in range(n):
        print(fuc(i))


