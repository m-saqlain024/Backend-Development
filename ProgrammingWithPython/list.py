list1 = [1,2,3,4,5,6]
list2 = ['a','s','d','f']
list3 = ['hello', 2,3.2,True]
list4 = [1,2,3,[4,5,6],7,8]


# print(*list2)

# for addin value to the list 
list2.insert(len(list2), 9)
list2.append(6)
list2.extend(['f','g','h'])

# print(*list2)

# print(list2,sep=" ")


# remove element from the list 

list5 = [1,2,3,4,5,6,7]
print(*list5)
list5.pop(2)
del list5[2]
print(*list5)