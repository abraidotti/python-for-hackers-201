# change the meaning of an operator depending on operands used

# simple example
print(1 + 1)
print("1" + "1")


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

    # overload the __str__ function
    def __str__(self):
        return "My name is {} and I am {} years old.".format(self.name, self.age)

    # overload the addition function for a special purpose
    def __add__(self, other):
        return self.age + other.age

    # Why overload mathematical operators? Semantic reasons
    # Let's make it easy to compare Person ages
    def __lt__(self, other):
        return self.age < other.age


bob = Person("bob", 30)
alice = Person("alice", 20)

print(bob)
print(bob.__dict__)
print(bob + alice)
print(bob < alice)
print(alice < bob)
