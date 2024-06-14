class myClass:
    a = 12
    # print('hello worlds')
    def Hello(self):
        print("hello world ")


myobj = myClass()
# print(myobj.a)
# print(myClass.a)

# print(myobj.Hello())



class House:
    numroom = 5
    kithen = 2
    def hello(self):
        print(self.numroom)
        pass

house = House()
print(house.hello())


bravo = 3
b = B()
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)