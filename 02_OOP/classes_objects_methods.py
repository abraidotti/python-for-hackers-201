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

    def birthday(self):
        self.age += 1


bob = Person("bob", 30)
alice = Person("alice", 20)
mallory = Person("mallory", 15)

print(bob)
print(alice)
print(mallory)

alice.print_name()
bob.print_age()

print(bob.name)
print(hasattr(bob, "age"))
print(hasattr(bob, "sex"))

print(getattr(bob, "age"))
setattr(bob, "age", 22)
print(getattr(bob, "age"))

setattr(bob, "sex", "m")
print(getattr(bob, "sex"))

# delattr(bob, "sex")
print(bob.sex)

print(Person.wants_to_hack)
Person.wants_to_hack = "No"
print(bob.wants_to_hack)

bob.print_age()
bob.birthday()
bob.print_age()

Person.my_class_method()
# bob.my_class_method() # error

# you can delete a whole class
# del Person
# alexa = Person("alexa", 38)

print(Person.__dict__)  # namespace dictionary
print(Person.__doc__)  # docstring
print(Person.__name__)  # class name
print(Person.__module__)  # module in the file
