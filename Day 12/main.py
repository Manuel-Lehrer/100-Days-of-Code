import random
from art import logo


Game_over = False


def random_number():
    return random.randint(1, 100)


def check_guess(guess, answer):
    if guess > answer:
        print("Too high.\n")
    elif guess < answer:
        print("Too low.\n")
    else:
        print(f"You got it. The number was {answer}")
        global Game_over
        Game_over = True


def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.\n")
    answer = random_number()

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()

    if difficulty == "easy":
        amount_attempts = 10
    elif difficulty == "hard":
        amount_attempts = 5
    else:
        print("your input was invalid")

    global Game_over
    while Game_over == False:
        print(f"You have {amount_attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        check_guess(guess, answer)

        if guess != answer:
            amount_attempts -= 1

        if amount_attempts == 0:
            Game_over = True

        if Game_over == True:
            if amount_attempts > 0:
                print("Congrats man.\n")
            elif amount_attempts == 0:
                print(f"Damn, you ran out of Luck, better luck next time. The number was {answer}\n")

            if input("Would you like to play another game? If so, type 'yes' ") == 'yes':
                game()
            else:
                print("Goodbye :)")


game()
