import random

options = ("rock", "paper", "scissors")

option = random.choice(options)

while True:
    player = input("Enter a choice rock paper or scissors: ")
    if player == option:
        print("Its a tie go again")
    elif player == "rock" and option == "paper":
        print(f"Player 1 chooses {player} while Player 2 chooses {option}")
        print("Player 2 wins")
    elif player == "paper" and option == "scissors":
        print(f"Player 1 chooses {player} while Player 2 chooses {option}")
        print("Player 2 wins")
    elif player == "scissors" and option == "rock":
        print(f"Player 1 chooses {player} while Player 2 chooses {option}")
        print("Player 2 wins")
    else:
        print(f"Player 1 chooses {player} while Player 2 chooses {option}")
        print("Player 1 wins")
        break
