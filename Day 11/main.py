from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck_length = len(cards)

money = [1000]


def calc_money_win(money, bet_amount):
    money[0] += bet_amount
    print(f"Your bet was {bet_amount}$. Now you have {money}$")


def calc_money_lose(money, bet_amount):
    money[0] -= bet_amount
    print(f"Your bet was {bet_amount}. Now you have {money}")


def print_scores_cards(your_cards, current_score, computer_score, computers_cards):
    print()
    print(f"Your final hand: {your_cards}, final score: {current_score}")
    print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")


def basic_winner_check(current_score, computer_score):
    if current_score > computer_score:
        print_scores_cards(your_cards, current_score, computer_score, computers_cards)
        print("Congrats. You win!\n")
        calc_money_win(money, bet_amount)
    elif current_score < computer_score:
        print_scores_cards(your_cards, current_score, computer_score, computers_cards)
        print("Fucking unlucky. You lose.\n")
        calc_money_lose(money, bet_amount)
    else:
        print_scores_cards(your_cards, current_score, computer_score, computers_cards)
        print("Guess its a draw.\n")


def check_winner(current_score, computer_score, computers_cards):
    if current_score > computer_score:
        if computer_score > 16:
            basic_winner_check(current_score, computer_score)

        else:
            while computer_score < 17:
                new_computer_card = random_card()
                computer_score += new_computer_card
                computers_cards.append(new_computer_card)
            if computer_score > 21:
                for cards in computers_cards:
                    if cards == 11:
                        computers_cards[computers_cards.index(11)] = 1
                        computer_score -= 10
                print_scores_cards(your_cards, current_score, computer_score, computers_cards)
                print("The computer busted. You win\n")
                calc_money_win(money, bet_amount)
            else:
                basic_winner_check(current_score, computer_score)

    else:
        basic_winner_check(current_score, computer_score)


def random_card():
    return cards[random.randint(0, deck_length - 1)]


def another_card(current_score, your_cards, computer_score, computers_cards):
    if input("Type 'y' to get another card, type 'n' to pass: ") == "y":

        next_card = random_card()

        your_cards.append(next_card)

        current_score += next_card

        if current_score > 21:
            for cards in your_cards:
                if cards == 11:
                    your_cards[your_cards.index(11)] = 1
                    current_score -= 10
            if current_score < 21:
                print(f"Your Cards: {your_cards}, current score: {current_score}.")
                another_card(current_score, your_cards, computer_score, computers_cards)

            else:
                print_scores_cards(your_cards, current_score, computer_score, computers_cards)
                print(f"Score :{current_score} You busted! Go home man.\n")
                calc_money_lose(money, bet_amount)


        elif current_score == 21:
            check_winner(current_score, computer_score, computers_cards)
        else:
            print(f"Your Cards: {your_cards}, current score: {current_score}.")
            another_card(current_score, your_cards, computer_score, computers_cards)
    else:

        check_winner(current_score, computer_score, computers_cards)


start = True
while start == True:
    print(logo)
    want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower().strip()
    if want_play == "y":

        bet_amount = int(input(f"Currently you have {money}$ How much do you want to bet?: $"))

        first_card = random_card()
        second_card = random_card()

        first_card_computer = random_card()
        second_card_computer = random_card()

        your_cards = [first_card, second_card]
        computers_cards = [first_card_computer, second_card_computer]

        current_score = first_card + second_card
        computer_score = first_card_computer + second_card_computer

        if current_score == 21:
            check_winner(current_score, computer_score, computers_cards)
        else:
            print(f"Your Cards: {your_cards}, current score: {current_score}")
            print(f"Computer's first card: {computers_cards[0]}")
            another_card(current_score, your_cards, computer_score, computers_cards)

    else:
        start = False
        print("Your better off this way. Gamba is bad. See ya...")