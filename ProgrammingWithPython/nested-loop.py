import time
Start_Time = time.time()



list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]


count = 0
for x in list1:
    count = count+1
    for y in list2:
        count = count+1 
        # print(count)

for x in range(10):
    for y in range(10):
     print(y, end=" ")
    print(x)


print(round(time.time() - Start_Time),2)