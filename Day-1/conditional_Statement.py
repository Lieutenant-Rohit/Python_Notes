# if else Statement
from operator import truediv

age = int(input("What is your age: "))
if age>100:
    print("You don't need credit card.")

elif age < 0:
    print("You haven't been born yet.")

elif age>18:
    print("You are eligible for credit card.")

else:
    print("You are not eligible for credit card.")


response = input("Would you like to have some food? (yes/no): ")
if response == "yes":
    print("Have some food.")
else :
    print("No food for you.")

name = input("What is your name: ")
if name == " ":
    print("You did not type any name")
else :
    print(f"Hello {name}.")

for_sale = True
if for_sale:
    print("This item is for sale")
else :
    print("This item is not for sale")