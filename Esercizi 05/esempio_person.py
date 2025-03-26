class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age - 2
    
    @age.setter
    def age(self, new_age):
        if new_age < 30:
            self.__age = new_age
        else:
            print("Never! I am always under 30!")

person = Person("Josiah Wang", 50)
print(person.age)
person.age = 10
print(person.age)
person.age = 70
print(person.age)
print(person.__age)

