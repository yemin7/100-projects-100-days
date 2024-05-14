import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

user_choice = input("What do you choose? Rock, Paper, or Scissors\n").lower()
user = 0

if user_choice == "rock":
    user = 0
elif user_choice == "paper":
    user = 1
elif user_choice == "scissors":
    user = 2

computer = game.index(random.choice(game))

print(f"Computer chose\n{game[computer]}")
print(game[user])

if user == 2 and computer == 0:
    print("You lose")
elif user == 0 and computer == 2:
    print("You win")
elif user < computer:
    print("You lose")
elif user > computer:
    print("You win")
else:
    print("Draw")
