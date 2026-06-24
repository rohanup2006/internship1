import random

options = ("rock","paper","scissors")
running = True

while running:
   
 player = None
 computer = random.choice(options)

while player not in options:
   player = input("enter a choice(rock,paper,scissors):")
print(f"player:{player}")
print(f"computer:{computer}")
if player == computer:
   print("it's a tie!")
elif player == "rock" and computer == "paper":
   print("computer win ")
elif player == "paper" and computer =="rock":
   print("player wins")
elif player == "rock" and computer == "scissors":
   print("player wins")
elif player == "paper"  and computer == "scissors":
   print("computer wins")
elif player == "scissors" and computer == "rock":
   print("computer wins")
elif player == "scissors" and computer == "paper":
   print("player wins")
else:
   print("invalid")   

play_again = input("play again? (y/n):").lower()
if not play_again == "y":
   running = False
   

print("thanks for playing")   

   