from art import logo, vs
from game_data import data
import random

# Only playable for uncultured individuals.
# Slight altercation from the original game, where you keep guessing with the higher option from the previous round.

print(logo)

previous_winner = ["?"]
winner_name = ["?"]


def random_celeb():
    celeb = random.choice(data)
    return celeb


def check_choice(celebA, celebB, choice, score):
    if choice == "a":
        if celebA["follower_count"] > celebB["follower_count"]:
            print(logo)
            print("You chose right congrats")
            previous_winner[0] = "A"
            winner_name[0] = celebA
            return True
        else:
            print(f"That was false. You lost. Final score: {score}")
            return False
    else:
        if celebA["follower_count"] < celebB["follower_count"]:
            print(logo)
            print("You chose right congrats")
            previous_winner[0] = "B"
            winner_name[0] = celebB
            return True
        else:
            print(f"That was false. You lost. Final score: {score}")
            return False


def celebs_vs():
    global celebA, celebB

    celebA = random_celeb()
    print(celebA["name"], ",", celebA["description"], ",", celebA["country"])

    print(vs)

    celebB = random_celeb()
    print(celebB["name"], ",", celebB["description"], ",", celebB["country"])

    if celebA == celebB:
        celebs_vs()


def celebs_vs_winner(previous_winner):
    global celebrityA, celebrityB
    celebrityA = previous_winner
    print(celebrityA["name"], ",", celebrityA["description"], ",", celebrityA["country"])

    print(vs)

    celebrityB = random_celeb()
    print(celebrityB["name"], ",", celebrityB["description"], ",", celebrityB["country"])

    if celebrityA == celebrityB:
        celebs_vs_winner(previous_winner)

    return celebrityA, celebrityB


score = 0

celebs_vs()

choice = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

if check_choice(celebA, celebB, choice, score) == False:
    start = False

else:
    next_round = True
    while next_round == True:
        score += 1
        if previous_winner[0] == "A":
            celebs_vs_winner(previous_winner=winner_name[0])
            choice = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
        elif previous_winner[0] == "B":
            celebs_vs_winner(previous_winner=winner_name[0])
            choice = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

        if check_choice(celebA=celebrityA, celebB=celebrityB, choice=choice, score=score) == False:
            next_round = False