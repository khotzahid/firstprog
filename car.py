class Car :
    def __init__(self,name,color,seater,price,expensive):
        self.name = name
        self.color = color
        self.seater = seater
        self.price = price
        self.expensive = expensive

car1 = Car("Honda","Green",4,3000,False)
print(car1.expensive)