file1=open("file1.txt","r")
file2=open("file2.txt","w")
position=1
for x in file1:
    if position%2!=0:
        file2.write(str(x))
    position=position+1
file1.close()
file2.close()