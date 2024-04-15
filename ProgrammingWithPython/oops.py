num1 = abs(13.2)

# print(num1)

def all(iterable):
    for x in iterable:
        if x:
            return True
    return False

num2 = all("")
print(num2)