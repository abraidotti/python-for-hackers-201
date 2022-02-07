# strings have len and arrays have len
# different methods but same name
# len is polymorphic
print(len("string"))
print(len(["l", "i", "s", "t"]))


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

people = [bob, alice]

for person in people:
    person.print_name()
    print(type(person))


def obj_dump(object):
    object.print_name()
    print(object.age)
    object.birthday()
    print(object.age)
    print(object.__class__)
    print(object.__class__.__name__)


obj_dump(bob)
obj_dump(alice)
