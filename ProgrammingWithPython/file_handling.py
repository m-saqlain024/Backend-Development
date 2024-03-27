file = open('test.txt',mode='r')


data = file.readline()

# print(data)

file.close()


with open('test.txt', mode='r') as file:
    datas = file.readline()
    print(datas)