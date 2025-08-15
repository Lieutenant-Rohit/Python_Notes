#Concession stand program
import time
menu = {"pizza":10.00,
        "burger":7.00,
        "popcorn":15.00,
        "fries":5.00,
        "nachos":4.50,
        "lemonade":3.00,
        "cold-Drink":5.00}

cart = {}
total = 0
print("----------MENU----------")
for key,value in menu.items():
    print(f"{key:15}: ${value:.2f}")
print("------------------------")

while True:
    food = input("What food would you like to have?(PRESS Q --> QUIT): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.update({food: menu[food]})
    else :
        print("Sorry, You entered an invalid food!")
print("------------------------")
print("YOU ORDERED: ")
for key,value in cart.items():
    print(f"{key:15}: ${value:.2f}")
    total+=value
print("------------------------")

print(f"Your Total Bill is : ${total:.2f}")

print("-------------------------")
print("How Would You like to PAY!!....")
print("1--->Via UPI")
print("2--->Via CASH")
print("************SUMMER OFFER-> 5% off on Total Bill************")
choice = int(input("ENTER YOUR CHOICE: "))
if choice == 1:
  total = total - 0.05*total
  print(f"Your New Total Bill is : ${total:.2f}")
  print("PLEASE PROCEED WITH THE PAYMENT")
  time.sleep(3)
  print("Processing Payment")
  for x in reversed(range(1, 4)):
      print(x, end=".")
      time.sleep(1)

elif choice == 2:
    print("Cash Received")
else:
    print("Invalid Payment Choice")
print()
print("Payment Received")
print("-------------------------")
print("Thank You for Ordering!")












