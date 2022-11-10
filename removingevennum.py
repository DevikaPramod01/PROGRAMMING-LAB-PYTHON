
list1=[]
odd=[]
n=int(input("enter list size : "))
for i in range(n):
    a=(int(input("Enter a number  :")))
    list1.append(a)
print("the orginal list is",list1)
odd=[each for each in list1 if each%2!=0]
print("the new list is",odd)
