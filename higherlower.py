from game_data import data
import random
from art import logo, vs


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_followers(guess, a_followers, b_followers):

    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
continue_game = True
account_b = random.choice(data)

while continue_game:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? 'A' or 'B': ").lower()


    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_followers(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You got the answer right! A: {a_followers} vs B: {b_followers}")
        print(f"Current Score: {score}\n")

    else:
        print(f"You got the answer wrong! A: {a_followers} vs B: {b_followers}")
        print(f"Final Score: {score}")
        continue_game = False

