import random

options = ('rock', 'paper', 'scissors')
player = None
computer = random.choice(options)
is_Playing = True


while is_Playing :


     player = input("Enter a choice (Rock, Paper, Scissors) (TYPE quit TO EXIT) ").lower()
     if player in options :
         print(f"You chose: {player}")
         print(f"Computer chose: {computer}")

         if player == computer:
             print("It's a Draw")
         elif player == 'rock' and computer == 'scissors':
             print("You Win")
         elif player == 'paper' and computer == 'rock':
             print("You Win")
         elif player == 'scissors' and computer == 'paper':
             print("You Win")
         else:
             print("You Lost")

     elif player == 'quit':
         print("Thank You for playing")
         is_Playing = False
     else:
         print("Invalid Choice")


