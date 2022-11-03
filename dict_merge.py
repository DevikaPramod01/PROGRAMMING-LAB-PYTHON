dict1={}
n=int(input("enter the num of items"))
for i in range(n):
    key=input("enter keys")
    value=input("enter value")
    dict1[key]=value
print("first dictionary is",dict1)

dict2={}
n1=int(input("enter the num of items"))
for i in range(n1):
    key=input("enter keys")
    value=input("enter value")
    dict2[key]=value
print("second dictionary is",dict2)

print("after merging dict1 with dict 2")
dict1.update(dict2)
print(dict1)
