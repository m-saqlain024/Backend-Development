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