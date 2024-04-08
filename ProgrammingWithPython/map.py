menu = ['assdf' , 'adgkhk','adkfjshk','ajhsdfjf','dkhdjf','hsjkdkjf']

def myfun(cofee):
    if cofee[0] == 'a':
        return cofee



menulsit = map(myfun , menu)

# print(menulsit)

# for x in menulsit:
    # print(x)


filter_menu = filter(myfun, menu)
for x in filter_menu:
    print(x)