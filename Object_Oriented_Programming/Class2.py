"""
Class Attibutes
Defined for the entire class
Not specific to any instance
"""

class Person:
    number_of_people = 0 #Class Attribute
    GRAVITY = -9.8
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod #Decorator
    def number_of_people_(cls): 
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        
p1 = Person("Susan")
p2 = Person("Jane")
print(Person.number_of_people_())