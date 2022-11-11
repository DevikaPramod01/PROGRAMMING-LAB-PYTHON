dict1={}
n=int(input("enter the no of items"))
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    dict1[key]=value

l=list(dict1.items())   #convert the given dict. into list
l.sort()                #sort the list
print("the sorted dictionay by keys:")
print("Ascending order is",l)
l=list(dict1.items())
l.sort(reverse=True)    #sort in reverse order
print("Descending order is",l)
