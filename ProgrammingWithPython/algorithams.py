# algorithams for plaindrame

# str = 'reacecae'

# start = 0
# last = len(str)-1


# print(str[start])
# print(str[last])



def isPalinders(str):
    start = 0
    last = len(str) -1
    for x in str:
        if str[start] != str[last]:
            return False
    return True


print(isPalinders('racecar'))