list1=[]
a=int(input("enter the size of the list1"))
for elem in range(a):
    b=input("enter the colors")
    list1.append(b)
list2=[]
c=int(input("enter the size of the list2"))
for elem in range(c):
    d=input("enter the colors")
    list2.append(d)
print("first list is",list1)
print("the second list is ",list2)
list3=[]
list3=[each for each in list1 if each not in list2]
print(list3)
