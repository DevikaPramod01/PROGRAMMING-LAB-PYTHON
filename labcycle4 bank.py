class bank:
    def __init__(self,a,n,t):
        self.acc_num=a
        self.name=n
        self.acc_type=t
        self.balance=0
        
    def deposit(self):
        amount=float(input("enter the amount to deposit " ))
        self.balance=self.balance + amount
        print("Rs.",amount,"deposited")
        
    def withdraw(self):
        amount=float(input("enter the amount to withdraw "))
        if amount>self.balance:
            print("Insufficient balance!")
        else:
            self.balance=self.balance-amount
            
    def check_balance(self):
        print("account balance is ",self.balance)

n=input("enter account name ")
a=input("enter account number ")
t=input("enter account type ")

acc1=bank(a,n,t)

while(1):
    print("Options ")
    print("1.deposit")
    print("2.withdraw")
    print("3.view account balance")
    print("4.Exit")
    c=int(input("enter a choice "))
    if c==1:
        acc1.deposit()
    elif c==2:
        acc1.withdraw()
    elif c== 3:
        acc1.check_balance()
    elif c== 4:
        break
    else:   
        print("wrong choice")
