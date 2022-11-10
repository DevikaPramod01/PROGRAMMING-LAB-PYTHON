string = input("Type a string : ")
char = string[0]
string = string.replace(char,'$')
print("the new text with replaced character",char+string[1:])
