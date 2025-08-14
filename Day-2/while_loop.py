#while loop = execute some code WHILE some condition remains true.

name = input("Enter your name: ")

while name == " ":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Your name is {name}")

#Taking input till user enter valid age
age = int(input("Enter your age: "))
while age < 0:
    print("Age cannot be negative")
    age = input("Enter your age: ")
print(f"Your age is {age}")


food = " "
while food != "Q":
    food = input("Enter your Favourite food(Q to quit): ")
    print(f"Your favourite food is {food}")


