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
# print(bob.age)

print(bob.get_age())
bob.set_age(31)
print(bob.get_age())
bob.birthday()
print(bob.get_age())

# circumvent encapsulation
print(bob.__dict__)
bob._Person__age = 50
print(bob.get_age())
