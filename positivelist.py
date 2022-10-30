a=[]
b=[]
n=int(input("enter the list size"))
for i in range(0,n):
    c=int(input("enter the list elements"))
    a.append(c)
print("the list is",a)
for i in a:
    if(i>0):b.append(i)
print("the positive integrs are",b)


