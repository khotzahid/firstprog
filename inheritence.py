class Fruits:
    def my_favorite(self):
        print("I like fruits")

    def it_is_healthy(self):
        print("Fruits are very healthy")

class Apple(Fruits):
    def my_price(self):
        print("Apple is very expensive")

    def my_color(self):
        print("Apple are red in color")

class Banana(Fruits):
    def my_price(self):
        print("Banana is cheap")

    def my_color(self):
        print("Banana are yellow in color")

fruits = Fruits()
apple = Apple()
banana = Banana()

banana.my_favorite()
apple.my_color()

