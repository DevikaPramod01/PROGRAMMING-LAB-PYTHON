def string(a):
    if a[-1]=="g" and a[-2]=="n" and a[-3]=="i":
        a.append("ly")
    else:
        a.append("ing")
    print(''.join(a))
j=list(input("enter the word"))
string(j)
