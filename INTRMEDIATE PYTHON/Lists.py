mylist = ["banana", "cherry", 35, "apple", 35]
print(mylist)
mylist.append("grapes")
print(mylist)
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

mylist.pop()
print(mylist)

mylist.remove(35) # Remove
print(mylist)

mylist.reverse() # Reverse
print(mylist)

mylist2 = [-234, 984.34, 76, 89, 12, 984, 267]
mylist2.sort() # sort
print(mylist2)

newlist = mylist + mylist2 #concatination with '+'
print(newlist)

a = mylist2[1:6] # slice operator
print(a)

#List comprehension
listnum = [1, 2, 3, 4, 5, 23, 45, 12]
b = [i * i for i in listnum]
print(listnum)
print(b)