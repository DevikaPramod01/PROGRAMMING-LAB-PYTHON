list=[]
num=int(input("how many colors do you want to enter"))
for i in range(num):
    a=input("enter the color ")
    a=a.split()
    list.append(a)
    print("the entered colors are",list)
print("first color is ",list[0],"\n last color is ",list[-1])
