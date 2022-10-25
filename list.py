a=[]
b=[]
n=int(input("enter the size of first list"))
for i in range(1,n+1):
    c=int(input("enter the list element of a "))
    a.append(c)
m=int(input("enter the size of second list"))
for i in range(1,m+1):
    d=int(input("enter the list element of b"))
    b.append(d)
print("list 1 is",a)
print("list 2 is",b)
print("\n 1.check whether the lists are of same value\n 2.check whether the lists sums to same value\n3.check whether any value occur in both list\n");
if(n==m):print("the lists are of same length")
else:print("the list are of different size")
total=sum(a)
total1=sum(b)
if(total==total1):print("the list sums to same value")
else:print("the list sums to different values")
c=[]
flag=0
for elem in a:
    if elem in b:
        flag=1
        c.append(elem)
if flag==1:print("values",c,"occur")
else:print("values not occur")
