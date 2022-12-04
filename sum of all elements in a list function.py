def sum(list):
    sum=0
    for x in list:
        sum=sum+x
    return sum
size=int(input("enter the limit:"))
list1=[]
for _ in range(size):
    a=int(input("enter the list element"))
    list1.append(a)


print("sum is",sum(list1))
