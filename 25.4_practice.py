# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def talk(self):
#         print("Talk")
        

# galib = Person("Asadullah Al Galib")

# galib.talk()
# print(galib.name)



class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name}")
        

galib = Person("Asadullah Al Galib")
galib.talk()

labib = Person("Mahmudullah Al Labib")
labib.talk()