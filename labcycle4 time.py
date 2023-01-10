class Time:
    def __init__(self,hour,minute,second):
        self._hour=hour
        self._minute=minute
        self._second=second
    def __add__(self,other):
        hour=self._hour+other._hour
        if hour>=24:
            hour=hour%24
        minute=self._minute+other._minute
        if minute>=60:
            hour+=1
            minute=minute%60
        second=self._second+other._second
        if second>=60:
            minute+=1
            second=second%60
        return Time(hour,minute,second)
    
    def view_time(self):
        print(self._hour,":",self._minute,":",self._second)        
t1=[int(i) for i in input("enter time1 ").split(":")]
t2=[int(i) for i in input("enter time2 ").split(":")]

time1=Time(t1[0],t1[1],t1[2])
time2=Time(t2[0],t2[1],t2[2])
sum=time1+time2

print("time1= ",end=" ")
time1.view_time()

print("time2= ",end=" ")
time2.view_time()

print("sum ",end=" ")
sum.view_time()
