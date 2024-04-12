import random
import os
from art import logo, vs
from game_data import data


score = 0

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type A or B: ").lower()
    won = False

    if account_a["follower_count"] > account_b["follower_count"]:
        if guess == 'a':
            score = score + 1
            print("Yes, you are correct!!! and your score is", score)
            won = True
            account_a = account_b
            account_b = random.choice(data)
        else:
            print("Sorry, better luck next time!!! and your score is", score)
    else:
        if guess == 'b':
            score = score + 1
            print("Yes, you are correct!!! and your score is", score)
            won = True
            account_a = account_b
            account_b = random.choice(data)
        else:
            print("Sorry, better luck next time!!! and your score is", score)

    if not won:
        break