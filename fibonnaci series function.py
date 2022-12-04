def fibo(n):
    first=0
    second=1
    if n==1:print(first)
    else:
        print(first)
        print(second)
        n=n-2
        while(n):
             third=second+first
             first=second
             second=third
             n-=1
             print(third)
n=int(input("enter limit:"))
fibo(n)
