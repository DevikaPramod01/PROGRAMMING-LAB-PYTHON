list=[]
n=int(input("enter the size of the list"))
for i in range (0,n):
    b=int(input("enter integer numbers"))
    list.append(b)
print("the orginal list is",list)
for elem in list:
    if(elem%2==0):
        list.remove(elem)
print("the new list is",list)
