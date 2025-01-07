class A:
    print("LIST A")

class B:
    print("LIST B")


class C(A,B):
    print('HELLO C')

class Parent:
    def greet(self):
        print("Hello this parent")

class Child(Parent):
    def greet(self):
        print("Hello this Child")


ch = Child().greet()

class Car:
    def __init__(self, model):
        self.__model = model
    
    def get_model(self):
        return self.__model


print(Car("Hello").__model)