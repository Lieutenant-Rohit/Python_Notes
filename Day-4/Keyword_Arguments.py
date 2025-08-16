#Keyword arguments = an argument preceded by an identifier
#                    helps with readability
#                    Order of argument doesn't matter

def hello(greeting, title, first, last):
  print(f"{greeting} {title} {first} {last}")

hello("Hello","Mr","Bro","Code")

#Positional argument comes before keywords arguments.
hello("Hello", first = "Bro", title = "Mr", last = "Bro")

print("1","2","3","4",sep = "--")