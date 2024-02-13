questions = ("Who initially owned the straw hat: ",
             "What is the ancient weapon Poseidon: ",
             "What is Law's full name: ",
             "What race is Kuma from: ",
             "What happened are the end of Thiller Bark when Kuma took Zoro away: ")

options = (("A. Shanks", "B. Rocks", "C. Roger", "D. Whitebeard"),
           ("A. A warship", "B. Sea Kings", "C. A Devil Fruit", "D. A mermaid"),
           ("A. Trafalgar D. Water Law", "B. Trafalgar Water Law", "C. Trafalgar Corazon Law", "D. Trafalgar Law"),
           ("A. Shandia", "B. Kuja", "C. Lunarian", "D. Buccaneer"),
           ("A. Zoro took Luffy's pain", "B. Zoro fought Kuma", "C. Zoro was killed by Kuma", "D. ..."))

answers = ("C", "D", "A", "D", "D")

guesses = []

score = 0
questionNum = 0

print("-----One Piece Trivia Questions-----")
print("How well do you know One Piece")

for question in questions:
    print("-------------------------------------")
    print(question)
    for option in options[questionNum]:
        print(option)


    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questionNum]:
        score += 1
        print("CORRECT!!!!!")
    else:
        print("INCORRECT :(")
        print(f"{answers[questionNum]} is the correct answer")
    questionNum += 1

print("--------------------------")
print("         RESULTS          ")
print("--------------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

if score < 70:
    print(f"Dude you call yourself a One Piece fan yet you got a {score}% "
          f"on behalf on the One Piece community we disown you")
elif score > 70 and score <= 89:
    print(f"Well you passed with a {score}% but you could've done better")

elif score > 90 and score <= 99:
    print(f"Huh you did pretty good you got a {score}% but that's to be expected from anyone who calls themselves a fan")

else:
    print(f"I expected no less from a genuine fan Congrats you got a {score}% ")
