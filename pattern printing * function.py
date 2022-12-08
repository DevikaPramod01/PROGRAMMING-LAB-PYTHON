def pattern():
    k=1
    for i in  range(1,10):
        if i<6:
            for j in range(1,i+1):
                print("* ",end="")
            print("\n")
        else:
            for j in range(1,i-k):
                print("* ",end="")
            print("\n")
            k=k+2

pattern()
