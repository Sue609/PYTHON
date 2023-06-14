'''class Dog:
    
    def __init__(self, name):
        self.name = name
        print(name)
    
    def bark(self):
        print("bark")
        
d = Dog("bako")
d.bark()
print(type(d))'''



class User:
     id = 89
     name = "no name"
     __password = None
     
     def __init__(self, new_name=None):
         self.is_new = True
         if new_name is not None:
             self.name = new_name
 
u = User()
u.is_new