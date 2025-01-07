class Person:
    name = "Rahat"

    def change_name(self, name):
        self.__class__.name = name

p1 = Person()
p1.change_name("Minhazur")
print(p1.name)
print(Person.name)


class Person2:
    name = "Rahat"

    @classmethod
    def change_name(cls, name):
        cls.name = name 

p2 = Person2()
p2.change_name("Name")
print(p2.name)
print(Person2.name)