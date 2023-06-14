from item import Item

class Phone(Item):
       
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #call to super function to have access to all atributes/methods
        super().__init__(
            name, price, quantity
        )       
        
        #run validations to the received arguements 
        assert broken_phones>= 0, f"broken Phones {broken_phones} is not greater or equal to zero!"
        
        
        # assign to self object
        #assigning attributes to instances
        self.broken_phones =broken_phones
        
        #assert #statement key word used to check if there is a match between what is happening and to your expectations.
    