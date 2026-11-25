class Rectangle:
    def __init__(self, name):
        print(f"\nEnter length and breadth of {name}")
        self.l = int(input("Enter length: "))
        self.b = int(input("Enter breadth: "))        
    def area(self):
        return self.l * self.b         
    def perimeter(self):
        return 2 * (self.l + self.b)        
    def __lt__(self, r):
        return self.area() < r.area()
r1 = Rectangle("r1")
r2 = Rectangle("r2")
if r1 > r2:
    print("\nr1 is greater")
else:
    print("\nr2 is greater")

