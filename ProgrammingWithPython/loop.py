# for i in range(100):
    # print("looping" , i)

cars = ["Ford", "Volvo", "BMW"]


for item in cars:
    print("my favourite item " , item)

count = 0
while  count < len(cars):
    print("i like this cars", cars[count])
    count = count+1


favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break
    else:
        print('No sorry, not a dessert on my list')


print("next example start")
for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)


print("pass example ")


for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)