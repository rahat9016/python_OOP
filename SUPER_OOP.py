class Car:
    def __init__(self, type):
        self.type = type
    

class Toyota(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        

v1= Toyota("V1", "vvvv")
print(v1.type)