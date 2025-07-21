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

game_images = [rock, paper, scissors]
user = int(input("What is your selection?(0 for rock, 1 for paper, 2 for scissors): "))
print(game_images[user])
computer_choice = random.randint(0, 2)
if user>2 or user<0:
    print("Invalid input. Please try again.")
elif ((user == 0 and  computer_choice==0) or
    (user == 1 and computer_choice==1)
        or (computer_choice == 2 and user == 2)):
    print("It is a Tie!!!!\n", game_images[computer_choice])
elif ((user == 0 and computer_choice==2) or
    (user == 2 and computer_choice==1) or
(user == 1 and computer_choice==0)):
    print("You Win\n", game_images[computer_choice])
else:
    print("You Lose\n", game_images[computer_choice])
