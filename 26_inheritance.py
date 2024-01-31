class Mammal:
    def walk(self):
        print("Walk")
        
class Dog(Mammal):
    pass # if theres no methods in class error: So we write pass so no error occurs

class Cat(Mammal):
    def meow(self):
        print("Meow Meow")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.meow()
cat1.walk()