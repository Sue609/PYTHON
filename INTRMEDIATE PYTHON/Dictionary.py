'''
Dictionary - They are key-Value pairs, Unordered, Mutable.
Created with braces '{}' and separet items with ':'
'''

mydict = {
    "name": "Susan",
    "age": 23,
    "city": "New York"    
}
print(mydict)

mydict2 = dict(name="Laylah", age=2, city="Boston")
print(mydict2)

del mydict2["age"]
print(mydict2)