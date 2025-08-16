##Function = A block of reusable code
##             Place () after the function name to invoke it
def happy_birthday(name,year):
    print(f"Happy Birthday to you {name}")
    print(f"You are {year} years old {name}!!!")
    print(f"Happy Birthday to you {name}!!!")
    print()

happy_birthday("bro",30)
happy_birthday("sis",23)


#Return = statement used to end a function and send a result back to the caller

def average(a , b):
    return (a+b)/2

avg = average(3,4)
print(f"Average of Numbers 3 and 4 is {avg}")



