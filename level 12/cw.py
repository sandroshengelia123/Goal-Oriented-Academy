

choices = ["rock","paper", "scissors",]

user_choice = input("Enter your choice(rock, paper, or scissors):").lower()
computer_choice = random. choice(choices)

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tiel)
elif (user_choice == 'rock' and computer_choice == 'scissors') or /
     (user_choice == 'paper'and computer_choice == 'rock') or /
     (user_choice == 'peper'and computer_choice == 'peper'):
    print("you win")
else:
     print("computer_wins!")
