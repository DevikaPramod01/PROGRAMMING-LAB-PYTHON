text=input("enter a text")
text=text.split()
i=0
while i<len(text):
    count=0
    for word in text:
        if text[i]==word:
            count=count+1
    print(text[i],"\t present",count,"times")
    i=i+1
