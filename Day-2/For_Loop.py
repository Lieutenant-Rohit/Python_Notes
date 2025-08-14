#For Loop = executes a block of code a fixed number of times.
#Second number in range is exclusive
for x in range(1,11):
    print(x)

print("Congratulations! You have successfully executed for loop!.. :)")

#if we want to count by steps
for x in range(1,11,2):
    print(x)

#iterating over a string
credit_card = "1234-2344-2131-4543"
for x in credit_card:
    print(x)

for x in range(1,20):
    if x == 13:
        continue
    else:
        print(x)