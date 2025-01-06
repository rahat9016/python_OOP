class A:
    print("LIST A")

class B:
    print("LIST B")


class C(A,B):
    print('HELLO C')


d = C()
# print(d)