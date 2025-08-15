#QUIZ GAME

questions = ("How many elements are in the periodic table?:",
             "Which animal lays the largest egg?: ",
             "What is the most abundant gas in Earth's atmosphere?:",
             "How many bones are there in a human body?: ",
             "Which is the hottest planet in the solar system?: ",)

options = (("A: 116","B: 117","C: 118","D: 119"),
           ("A: Elephant","B: Whale","C: Crocodile","D: Ostrich"),
           ("A: Nitrogen","B: Oxygen","C: Carbon-Dioxide","D: Hydrogen"),
           ("A: 206","B: 207","C: 208","D: 209"),
           ("A: Mercury","B: Venus","C: Earth","D: Jupiter"))

correct_answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    my_answer = input("Enter your answer: ").upper()
    guesses.append(my_answer)
    if my_answer == correct_answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    question_num += 1
print("-----------------------------")
print("Correct Answers:",end=" ")
for correct_answer in correct_answers:
    print(correct_answer,end=" ")
print()
print("Guesses",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()
print("-----------------------------")
score = score/len(guesses)*100
print()
print("Your score is:",score,"%")
print("Thank you for playing!")


