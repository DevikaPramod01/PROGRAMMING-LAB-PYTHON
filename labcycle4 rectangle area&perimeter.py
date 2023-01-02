
class rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length+ self.breadth)

l1=int(input("enter length 1 "))
b1=int(input("enter breadth 1 "))
l2=int(input("enter length 2 "))
b2=int(input("enter breadth 2 "))

rect1=rectangle(l1,b1)
rect2=rectangle(l2,b2)

print("area of rectangle 1:",rect1.area())
print("perimeter of rectangle 1:",rect1.perimeter())
print("area of rectangle 2:",rect2.area())
print("perimeter of rectangle 2:",rect2.perimeter())
print("\n comparing rectangles....")

if rect1.area()==rect2.area():
    print("\n area of rectangles are equal")
else:
    print("\n area of rectangles are different")
if rect1.perimeter()==rect2.perimeter():
    print("\n perimeter of rectangles are equal")
else:
    print("\n perimeter of rectangles are different")

               
        
            
	

