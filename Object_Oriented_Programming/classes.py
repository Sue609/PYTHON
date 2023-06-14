#When we create functions inside classes they are called METHODS
#__init__: This is a constructor
#You can assign attributes to specific istances individually


from item import Item
from phone import Phone

item1 = Item("MyItem", 750)
item1.name = "OtherItem"

print(item1.read_only_name)
