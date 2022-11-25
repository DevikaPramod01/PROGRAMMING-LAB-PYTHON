def fibonnaci(n):
    if(n<=1):return n
    else:return fibonnaci(n-1)+fibonnaci(n-2)
n=int(input("enter the limit"))
if(n<=0):print("invalid limit")
else:print("the fibonnaci series is")
for i in range(0,n):
    print(fibonnaci(i))
