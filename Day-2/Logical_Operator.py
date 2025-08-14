#Logical Operator - used for conditional statements

# and = checks two or more condition if True
# or = checks if at least one condition is True
# not = True if condition is False or Vice-Versa

# temp = 25
# if 20 < temp < 30:
#     print("Temperature must be between 20 and 30")
#
# elif 30 < temp < 40:
#     print("Temperature must be between 30 and 40")
#
# elif temp < 0:
#     print("Its Fucking Cold!....")

temp = float(input("Enter temperature in Celsius: "))

if temp > 30:
    print("To Hot to Handle!...")

elif temp >20 and temp <=30:
    print("Its Hot")

elif temp>15 and temp<=20:
    print("Its Normal")

else:
    print("Its Cold")

sunny = True
if not sunny:
    print("It is not Sunny")
else :
    print("It is Sunny")



