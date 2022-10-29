a=[]
n=int(input("enter the size of the list"))
for i in range(0,n+1):
    b=int(input("enter a number"))
    a.append(b)
c=[]
for i in a:c.append(i**2)
print("the square of",a,"is",c)
