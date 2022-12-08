def length(k):
    count=0
    for i in k:
        s=0
        for j in i:
            s+=1
        if s>count:
            count=s
    return(count)
y=list(input("enter the string separated by space :").split(" "))
print(f"the length of longest word in the list is {length(y)}")
