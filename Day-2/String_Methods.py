# # #string function
# #
# # name = input("What is your name?")
# #  #Len() - Finds length
# # result = len(name)
# # print(result)
# #
# # #Find() - finds first occurrence of something.
#
# # result = name.find("r")
# # print(result)
# #
# # #rfind() - last occurrence of something
# # result = name.rfind("r")
# # print(result)
# #
# # #Capitalize -> First letter capital
# # result = name.capitalize()
# # print(result)
# #
# # #Upper and lower case
# # result = name.upper()
# # print(result)
# # result = name.lower()
# # print(result)
# #
# # #isdigit() -> if string contains only digit
# # result = name.isdigit()
# # print(result)
# #
# # #isalpha() -> return boolean if string contains only alphabets.
# # result = name.isalpha()
# # print(result)
# #
# # phone_Number = input("What is your phone number?")
# # #count() -> used to count the amount of something in a string
# # result = phone_Number.count("-")
# # print(result)
# #
# # #replace() -> replaces something with something
# # result= phone_Number.replace("-"," ")
# # print(result)
# #
# # print(help(str))
# #
# # #Validate user input
# # #1-> Username is no more than 12 characters
# # #2-> username must not contain spaces
# # #3-> username must not contain digit
# #
# username = input("What is your name?")
# if len(username) > 12:
#     print("Your name is too long")
#
# elif not username.isalpha():
#     print("You cant enter digit in username")
#
# elif username.find(" ") != -1:
#     print("You cant enter space in username")
#
# else:
#     print(f"You have entered a valid username: {username}")
#
#
# #Indexing = accessing elements of a sequence using [] (indexing operator) [Start :End]

credit_card="2313-1323-4353-5345"
print(credit_card[5:9])

#if we pass negative number then compiler will access character from last
# :: -> steps prints every 2nd character in a string
print(credit_card[::2])

#accessing last 4 digits in credit card number
last_digit = credit_card[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}")

#to reverse a string set :: -1
print(credit_card[::-1])

