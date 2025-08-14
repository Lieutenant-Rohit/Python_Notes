email = input("Enter Email Address: ")

index = email.index("@")
username = email[:index]
domain = email[index+1:]
print(f"Username: {username}")
print(f"Domain: {domain}")