def factorial(n):
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return(n*factorial(n-1))
'''recursive function that calls itself..Here, the function will recursively call itself by decreasing the value of the n.'''
n=int(input("enter the number to find the factorial"))
print("the factorial is",factorial(n))
    
