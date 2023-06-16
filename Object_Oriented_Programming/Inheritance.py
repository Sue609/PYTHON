"""
Inheritance in Python
"""
class Pet: # Parent class
     def __init__(self, name, age):
        self.name = name
        self.age = age
        
     def show(self):
        print(f"I am {self.name} and I am {self.age} years old!")

     def speak(self):
         print('I dont know how to speak!')
         

class Dog(Pet): # Child classes 
        
    def speak(self):
        print("Bark")
        
            
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color  
    
    def speak(self):
        print("Meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. I am {self.color} in color!")


        
p = Pet("Tim", 19)
p.speak()
d = Dog("Bill", 34)
d.speak()
c = Cat("Timmy", 23, "white")
c.show()