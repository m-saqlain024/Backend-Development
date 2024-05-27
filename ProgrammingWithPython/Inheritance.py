class A:
    a=1
class B:
    b=2
class C(A,B):
    pass
c= C()
print(c.a ,c.b)


class P:
    a=3
class C1(P):
    b=4
class C2(C1):
    pass

obj = C2()
print(obj.a,obj.b)