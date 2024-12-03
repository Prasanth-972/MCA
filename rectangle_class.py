class Rectangle:
    def __init__(self,length,breadth):
       self.length= length
       self.breadth= breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2* (self.length+self.breadth)
    def display(self):
        print(f"Area of rectangle:{self.area()}")
        print(f"Perimeter of rectangle: {self.perimeter()}")
    def compare_area(self,other):
        if self.area()==other.area():
            print("Rectangle are equal in area")
        elif self.area()>other.area():
            print("Rectangle 1 is greater in area than Rectangle 2.")
        else:
            print("Rectangle 2 is greater in area than Rectangle 1")
print("Enter dimentions of the first rectangle:")
length1=int(input("Enter length1:"))
breadth1=int(input("Enter breadth1:"))
rect1=Rectangle(length1,breadth1)
rect1.display()
print("Enter dimentions of second rectangle:")
length2=int(input("Enter length2:"))
breadth2=int(input("Enter breadth2:"))
rect2=Rectangle(length2,breadth2)
rect2.display()
rect2.compare_area(rect2)
