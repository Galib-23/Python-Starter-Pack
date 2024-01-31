# Here we use camel case for defining classes
class Point:
    def move(self):
        print("Move")
    
    def draw(self):
        print("draw")

point1 = Point() # point1 is an instance or object of the class Point
point2 = Point()

point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)
