### Question: A shopping application accepts only positive quantities. Handle an invalid quantity.

quantity = -5
try:
    if quantity <= 0:
        raise TypeError("Quantity must be positive")
    
    print("Order Quantity :",quantity)
except TypeError as error:
    print(error)