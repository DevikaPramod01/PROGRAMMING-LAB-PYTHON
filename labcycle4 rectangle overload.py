class Rectangle:
    def __init__(self,l,b):
        self._length=l
        self._breadth=b
    def area(self):
        self.area1=self._length*self._breadth
        return self.area1
    def __lt__(self,other):
        if self.area()<other.area():
            return 1
        else:
            return 0
l1=int(input("enter length 1 "))
b1=int(input("enter breadth 1 "))
l2=int(input("enter length 2 "))
b2=int(input("enter breadth 2 "))

rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)

print("area of rectangle1 ",rect1.area())
print("area of rectangle2 ",rect2.area())
print("\n comparing rectangles....")
if rect1<rect2:
    print("rectangle2 has a larger area")
else:
    print("rectangle1 has larger area")
