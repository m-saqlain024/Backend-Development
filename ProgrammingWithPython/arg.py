def sum(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


sum(1,2,3,4,5)

print(sum(1,2,3,4,4,5,3))



def sum(**kwargs):
    sum = 0
    for x,y in kwargs.items:
        sum += y
    return sum


