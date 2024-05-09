from art import logo

print(logo)
print("Welcome to the secret auction program.")
bids = {}
start = True


def find_winner(bids):
    highscore = 0
    for items in bids:
        if bids[items] > highscore:
            highscore = bids[items]
            winner = items
    print(f"The winner is {winner} with a bid of {highscore}")


while start == True:
    key = input("What is your name?: ")
    value = int(input("What's your bid?: $"))
    bids[key] = value

    choice = input("Are there any other bidders? Type 'yes' or 'no'.")

    if choice == "yes":
        start = True

    else:
        find_winner(bids)
        start = False