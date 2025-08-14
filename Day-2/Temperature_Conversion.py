unit = input("Enter Unit(C--> Celsius OR F--> Fahrenheit)\n")
temp = float(input("What temperature would you like to convert to? "))

if unit == "C":
    temp = (temp * 9)/5 + 32
    unit = "Fahrenheit"
    print(f"Temperature in {unit} is {round(temp, 1)}")
elif unit == "F":
    temp = (temp  - 32)*5/9
    unit = "Celsius"
    print(f"Temperature in {unit} is {round(temp, 1)}")

else:
    print("You didn't enter proper units")

