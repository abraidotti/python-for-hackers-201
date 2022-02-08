from os import stat


class Person:
    # docstring
    """make a person out of nothing!"""

    # class variable
    wants_to_hack = True

    # class method - inaccessible to objects due to no 'self' in definition
    def my_class_method():
        print("This is a class method.")

    # init method
    def __init__(self, name, age):
        self.name = name
        # encapsulate (protect) this variable by prefixing two underscores
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # make a method act like a property
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    @classmethod
    def wants_to(cls):
        return cls.wants_to_hack

    # create a bob factory
    @classmethod
    def bob_factory(cls):
        return cls("bob", 30)

    # static methods can't access class attributes or instance attributes
    # static methods do not need an instance
    @staticmethod
    def static_print():
        print("I am the same")

    # function
    def print_name(self):
        print("My name is {}".format(self.name))

    # function
    def print_age(self):
        print("My age is {}".format(self.age))

    # function
    def birthday(self):
        self.__age += 1


bob = Person("bob", 30)
print(bob.age)

bob.age = 50
print(bob.age)

# del bob.age
# print(bob.age)

print(Person.wants_to())

bob1 = Person.bob_factory()
bob2 = Person.bob_factory()
bob3 = Person.bob_factory()

bob1.print_name()
bob2.print_name()
bob3.print_name()

Person.static_print()
bob3.static_print()
