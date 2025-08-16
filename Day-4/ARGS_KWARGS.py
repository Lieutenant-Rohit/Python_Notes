# *args         = allows you to pass multiple non-keyword arguments ### It save parameter in a tuple
# **kwargs      = allows you to pass multiple keywords arguments.   ### It save parameter in a dictionary

def add(*args):
    total = 0
    for x in args:
        total += x
    print(total)


add(1,2,3,4)
add(1,4,32,54,12,3,2.0)

def name(*args):
    for arg in args:
        print(arg, end=" ")

name("Dr","Spongebob","Squarepants")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_address(street = "123PizzaStreet",
              city = "Dehradun",
              state = "Uttarakhand",
              zip = "248007")
