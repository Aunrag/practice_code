'''suppose there is a river. there are number of fishes in the river .
the bigger fishes eats the smaller fishes,bigger the fish is faster the speed.
fishes can only go down stream and not up stream.if there are n number of fishes in the river initially how many fishes will remain in the end.'''
'''
i am spider man
n=int(input("enter the number of fishes: "))
import array as arr
a=arr.array('i',[])
b=arr.array('I',[])
for i in range(0,n):
    c=int(input("enter the fish: "))
    a.append(c)
for i in range(0,n):
    p=len(a)
    for j in range (0,p-1):
        d=a[j]
        f=a[j+1]
        if d<f:
            b.append(d)
    g=len(b)
    for i in range(0,g):
        h=b[i]
        a.remove(h)
    for i in range(0,g):
        b.pop()
print("fishes are:",a)
'''
for i in range(1,11):
    print(i,"i am spiderman")
spidy
