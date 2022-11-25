def count(string):
    length=0
    string = string.split()
    for i in string:
        if len(i) > length:
            length=len(i)    
    return  length

str = input("Enter the string: ")
word = count(str)
print(word)
