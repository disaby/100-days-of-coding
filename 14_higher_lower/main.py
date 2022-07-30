from os import system
import time
import random
import sys

import art
import data


def new_game():
    global used, points
    used = []
    points = 0


def compare(n1, n2, ch):
    if ch == "a" and data.data[n1]["follower_count"] > data.data[n2][
            "follower_count"]:
        return (n1, True)
    elif ch == "b" and data.data[n1]["follower_count"] < data.data[n2][
            "follower_count"]:
        return (n2, True)
    return [None, False]


def print_person(n):
    name = data.data[n]["name"]
    description = data.data[n]["description"]
    country = data.data[n]["country"]
    print(f"* {name} *  {description}. From {country}\n")


def get_random():
    rand = random.randint(0, 49)
    for i in used:
        if i == rand:
            rand = random.randint(0, 49)
    return rand


def game(n1, n2):
    system("clear")
    print(art.logo)
    global points
    if points > 0:
        print(f"You are right! Current points: {points}\n")
    print("Compare A: ")
    print_person(n1)
    print(art.vs)
    print("Against B: ")
    print_person(n2)
    ch = None
    while ch != 'a' and ch != 'b':
        ch = input("Who has more followers? Type A or B: ").lower()

    if compare(n1, n2, ch)[1]:
        points += 1
        new_random = get_random()
        game(compare(n1, n2, ch)[0], new_random)
    else:
        print(f"You're wrong! Your score is {points}.\n")
        newg = input(
            "Do you want to start a new game? Type Y if you want. An other letter otherwise: "
        )
        if newg.lower() == 'y':
            main()
        else:
            print("We will wait you! )\n")
            time.sleep(4)
            sys.exit()


def main():
    new_game()
    rand1 = get_random()
    rand2 = get_random()

    while rand1 == rand2:
        rand2 = get_random()

    game(rand1, rand2)


main()

# need to recheck get_random() used[] loop