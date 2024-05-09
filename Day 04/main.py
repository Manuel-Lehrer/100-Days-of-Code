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

ASCII_art = [rock, paper, scissors]

choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper 2 for Scissor. \n"))

if choice > 2 or choice < 0:
    print("You are a bafoon!")

else:
    print(ASCII_art[choice])
    print("Computer chose:\n")

    computer_choices = [0, 1, 2]
    random_choice = random.choice(computer_choices)

    print(ASCII_art[random_choice])

    if choice == random_choice:
        print("It is a draw")
    elif choice == 0 and random_choice == 2:
        print("You win")
    elif choice == 1 and random_choice == 0:
        print("You win")
    elif choice == 2 and random_choice == 1:
        print("You win")
    else:
        print("You lose")