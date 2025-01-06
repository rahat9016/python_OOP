class Car:
    @staticmethod
    def start():
        print("Cart is star.")
    
    @staticmethod
    def stop():
        print('Cart is store')

class Toyota(Car):
    def __init__(self, name):
        self.name = name
    

    def __private_fn(self):
        print("OKKK")



t1 = Toyota("Big car")
print(t1.__private_fn)