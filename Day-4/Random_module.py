import random

low = 1
high = 100
number = random.randint(low, high)
# print(number)
#
# options = ('ROCK', 'PAPER', 'SCISSORS')
# option = random.choice(options)
# print(option)
#
# cards = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
# random.shuffle(cards)
# print(cards)
guesses = 0
while True:
    guess = int(input(f"Guess a number between {low} and {high}: "))
    guesses+=1
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Congratulations, your guess is correct.")
        break
print(f"You Guessed The Number in {guesses}th guesses")