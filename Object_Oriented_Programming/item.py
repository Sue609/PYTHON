import csv

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        #run validations to the received arguements 
        assert price >= 0, f"price {price} is not greater than or equal to zero!"     
        assert quantity >= 0, f"Quantiry {quantity} is not greater or equal to zero!"
        
        # assign to self object
        self.price = price
        self.quantity = quantity
        self.name = name  #assigning attributes to instances
        #assert #statement key word used to check if there is a match between what is happening and to your expectations.
        
        #actions to execute
        Item.all.append(self)
        
          
        
    def calculate_total_price(self):
        return self.price * self.quantity 
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    @classmethod        
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),                
            )
            
    @staticmethod       
    def is_integer(num):
        # we will count out the floats that are point zero
        # ie 5.o, 10.0 etc
        if isinstance(num, float):
            #count out the floats that are decimals
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
                       
    
    def __repr__(self):
        return f"Item('{self.__class__.__name__}', {self.price}, {self.quantity})"


    