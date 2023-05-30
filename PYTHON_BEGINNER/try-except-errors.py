#TRY & EXCEPT ERRORS

print('hey susan')

try:
    age = int(input('Age: '))
    income = 2000
    risk = income/age

except ZeroDivisionError:
    print("Age connaot be 0")
       
except ValueError:
    print('Invalid value')
    
#CLASSES
# We use class to define new type to model real type example: lists and dictionaries. 

numbers = [1, 2, 3, 5, 34, 23, 49]
class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
    
Point1 = Point()
Point1.draw()

Point1.x = 10
Point1.y = 20
print(Point1.x)
