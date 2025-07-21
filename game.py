from browser import document, window

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

def play_game(event):
    user = int(event.target.value)
    computer_choice = int(window.Math.floor(window.Math.random() * 3))

    output = f"\nYour choice:\n{game_images[user]}\n"
    output += f"Computer's choice:\n{game_images[computer_choice]}\n"

    if user == computer_choice:
        output += "It is a Tie!!!!"
    elif (user == 0 and computer_choice == 2) or \
         (user == 2 and computer_choice == 1) or \
         (user == 1 and computer_choice == 0):
        output += "🎉 You Win!"
    else:
        output += "💥 You Lose!"

    document["output"].textContent = output

document["rock"].bind("click", play_game)
document["paper"].bind("click", play_game)
document["scissors"].bind("click", play_game)
