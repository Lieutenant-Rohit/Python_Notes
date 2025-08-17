# Think of a Python file like a TV remote.
#
# •  If you press the button directly, the TV turns on.
# •  If someone else uses the remote in their setup, you don’t want your TV turning on automatically.
#
# That’s what if __name__ == "__main__" does — it checks who’s pressing the button.
def say_hello():
    print("Hello, Rohit!")

print("This always runs")

if __name__ == "__main__":
    print("This runs only when greet.py is run directly")

