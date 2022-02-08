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
        self.age = age

    # function
    def print_name(self):
        print("My name is {}".format(self.name))

    # function
    def print_age(self):
        print("My age is {}".format(self.age))

    # function
    def birthday(self):
        self.age += 1


class Hacker(Person):
    def __init__(self, name, age, cves):
        # refer to the base class without explicitly referencing it
        super().__init__(name, age)
        self.cves = cves

    def print_name(self):
        print("My name is {} and I have {} cves".format(self.name, self.cves))

    def total_cves(self):
        return self.cves


bob = Person("bob", 30)
alice = Hacker("alice", 20, 5)

bob.print_name()
alice.print_name()

print(bob.age)
print(alice.age)

bob.birthday()
alice.birthday()

print(alice.age)

# print(bob.total_cves()) # error
print(alice.total_cves())

print(issubclass(Hacker, Person))  # True
print(issubclass(Person, Hacker))  # False

print(isinstance(bob, Person))  # True
print(isinstance(bob, Hacker))  # False

print(isinstance(alice, Person))  # True
print(isinstance(alice, Hacker))  # True
