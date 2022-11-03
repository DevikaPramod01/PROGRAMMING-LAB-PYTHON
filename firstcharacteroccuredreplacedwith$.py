text=input("enter a string")
a=text[0]
text=text.replace(a,'$')
text=a+text[1:]
print(text)
