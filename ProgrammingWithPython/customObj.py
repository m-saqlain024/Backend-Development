class Recipe:
    def __init__(self, dish , item , time ) -> None:
        self.dish = dish
        self.item= item
        self.time = time

    def contents(self):
        print("the number of "+ str(self.item) + " and " + str(self.item) + \
              "and this " + str(self.time))


pizza = Recipe('pizza', ['cheese','bread','nothing'],54 )
tomato = Recipe('tomoto', ['sead','water','nothing'],5224 )


print(pizza.contents())
print(tomato.contents())

# Sample Solution code
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")