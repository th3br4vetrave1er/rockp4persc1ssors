import random

rock = """
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Howdy partner! Welcome to the ROCK, PAPER, SCISSORS GAME!")
gestures_list = [rock, paper, scissors]

player = input("Type: Rock, Paper or Scissors: ").lower()
computer = random.randint(0, 2)

if player == "rock":
    player = 0
elif player == "paper":
    player = 1
elif player == "scissors":
    player = 2
else:
    print("To play a game you need to choose between 3 objects! Rock, paper or scissors!")
    print("Try again please!")
    exit()

print("PLAYER CHOSE:")
print(gestures_list[player])
print("COMPUTER CHOSE:")
print(gestures_list[computer])

if player == computer:
    print("ITS A TIE!")
elif player == 0 and computer == 2:
    print("PLAYER WON!")
elif player == 1 and computer == 0:
    print("PLAYER WON!")
elif player == 2 and computer == 1:
    print("PLAYER WON!")
else:
    print("COMPUTER WON!")