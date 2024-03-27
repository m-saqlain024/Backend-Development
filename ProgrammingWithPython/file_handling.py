file = open('test.txt',mode='r')


data = file.readline()

# print(data)

file.close()


# with open('sample/test.txt', mode='+r') as file:
    # datas = file.readline()
    # print(datas)



with open('test.txt', mode='w') as file:
    file.writelines(['this is a first line\n', 'this is a second line\n', 'this is a third line\n'])
   #/n for new line


try:
    with open('test.txt', mode='a') as file:
       file.writelines(['this is a first line\n', 'this is a second line\n', 'this is a third line\n'])
except FileNotFoundError as e:
    print('Error' ,e)