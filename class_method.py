class Fruits:
    def __init__(self,name,color,quantity,price):
        self.name = name
        self.color = color
        self.quantity = quantity
        self.price = price

    def is_expensive(self):
        if self.price >= 5 :
            return True
        else:
            return False

fruits1 = Fruits("Apple","Red",10,6)
print(fruits1.is_expensive())