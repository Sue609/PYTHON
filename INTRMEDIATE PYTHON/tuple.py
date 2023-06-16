"""
Tuple is an ordered, imutable, and allows duplicate elements
Cannot be changed after creation.
The parenthesis are optional '()'
if you want to have one element you must still separete by a comma ','.

"""
mytuple = ("sus", 234, "Califonia", 1, 3, 5, 2, 4, 6, 7)
print(mytuple)

my_tuple = "Susan",
print(my_tuple)

item = mytuple[0]
print(item)

b = mytuple[2:5] #slicing a tuple
print(b)

c = mytuple[::2] #step in tuple
print(c)

tuple1 = ("susan", 23, "Califonia") # unpacking
name, age, city = tuple1
print(name)
print(age)
print(city)
