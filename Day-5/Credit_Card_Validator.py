#Python Credit Card Validator

#1. Remove any '-' or ' '
#2. Add all digit in the odd places from right to left
#3. Double every second digit from right to left
#          (if result is two-digit number)
#          add the two-digit number together to get a single digit
#4 Sum the total steps 2 and 3
#5. If sum is divisible by 10, the credit card is valid

#Step 1
card = input("Enter your credit card number: ")
new_card = card.replace("-","")
new_card = new_card.replace(" ","")
print(new_card)
sum_odd_digits = 0
new_card = new_card[::-1] #Reverse the string
#Step 2
for x in new_card[::2]:
    sum_odd_digits += int(x)

#Step 3
sum_even_digits=0
for x in new_card[1::2]:
    result = int(x) * 2
    if result >=10:
        sum_even_digits += 1 + result%10
    else:
        sum_even_digits += result
#Step 4
total = sum_odd_digits + sum_even_digits
#Step 5
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")




