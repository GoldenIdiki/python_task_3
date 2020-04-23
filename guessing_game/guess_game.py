import sys


def easy():
    guess_chance = 0
    guess_limit = 6
    guess_left = 6
    guess_option = list(range(1, 11))
    while guess_chance < guess_limit:
        try:
            print("")
            guess = int(input("Please make a guess: "))
        except ValueError:
            print("Please restart the game")
            print("MAKE SURE YOU ENTER A WHOLE NUMBER BETWEEN 1 AND 10 NEXT TIME")
            sys.exit()
        if guess not in guess_option:
            print("Please enter a number between 1 and 10")
            guess_chance += 1
            guess_left -= 1
            if guess_left == 1:
                print("You have 1 chance left, choose wisely")
            elif guess_left == 0:
                pass
            else:
                print("You have {} chances left".format(guess_left))
        if guess == guess_option[9]:
            print("You got it right!")
            break
        elif guess != guess_option[9] and guess in guess_option:
            print("That was wrong")
            guess_chance += 1
            guess_left -= 1
            if guess_left == 1:
                print("You have 1 chance left, choose wisely")
            elif guess_left == 0:
                pass
            else:
                print("You have {} chances left".format(guess_left))
    else:
        print("Game over!")


def medium():
    guess_chance = 0
    guess_limit = 4
    guess_left = 4
    guess_option = list(range(1, 21))
    while guess_chance < guess_limit:
        try:
            print("")
            guess = int(input("Please make a guess: "))
        except ValueError:
            print("Please restart the game")
            print("MAKE SURE YOU ENTER A WHOLE NUMBER BETWEEN 1 AND 20 NEXT TIME")
            sys.exit()
        if guess not in guess_option:
            print("Please enter a number between 1 and 20")
            guess_chance += 1
            guess_left -= 1
            if guess_left == 1:
                print("You have 1 chance left, choose wisely")
            elif guess_left == 0:
                pass
            else:
                print("You have {} chances left".format(guess_left))
        if guess == guess_option[14]:
            print("You got it right!")
            break
        elif guess != guess_option[14] and guess in guess_option:
            print("That was wrong")
            guess_chance += 1
            guess_left -= 1
            if guess_left == 1:
                print("You have 1 chance left, choose wisely")
            elif guess_left == 0:
                pass
            else:
                print("You have {} chances left".format(guess_left))
    else:
        print("Game over!")


def hard():
    guess_chance = 0
    guess_limit = 3
    guess_left = 3
    guess_option = list(range(1, 51))
    while guess_chance < guess_limit:
        try:
            print("")
            guess = int(input("Please make a guess: "))
        except ValueError:
            print("Please restart the game and MAKE SURE YOU ENTER A WHOLE NUMBER BETWEEN 1 AND 50 NEXT TIME")
            sys.exit()
        if guess not in guess_option:
            print("")
            print("Please enter a number between 1 and 50")
            guess_chance += 1
            guess_left -= 1
            if guess_left == 1:
                print("You have 1 chance left, choose wisely")
            elif guess_left == 0:
                pass
            else:
                print("You have {} chances left".format(guess_left))
        if guess == guess_option[40]:
            print("You got it right!")
            break
        elif guess != guess_option[40] and guess in guess_option:
            print("That was wrong")
            guess_chance += 1
            guess_left -= 1
            if guess_left == 1:
                print("You have 1 chance left, choose wisely")
            elif guess_left == 0:
                pass
            else:
                print("You have {} chances left".format(guess_left))
    else:
        print("Game over!")


print("WELCOME TO GOLDEN'S LUCKY NUMBER")
print("""
Select 1 for Easy mode
Select 2 for Medium mode
Select 3 for Hard mode
""")
try:
    level = int(input("Please select the level: "))
except ValueError:
    print("Please restart the game and CHOOSE YOUR DESIRED LEVEL BY SELECTING EITHER 1, 2, OR 3")
    sys.exit()
level_list = [1, 2, 3]
if level == level_list[0]:
    print("GOLDEN'S LUCKY NUMBER (EASY MOOD)")
    print("You have 6 chances to make the right guess")
    easy()
elif level == level_list[1]:
    print("GOLDEN'S LUCKY NUMBER (MEDIUM MOOD)")
    print("You have 4 chances to make the right guess")
    medium()
# If user inputs a number not in level_list,
# it will automatically bring up hard level
else:
    print("GOLDEN'S LUCKY NUMBER (HARD MOOD)")
    print("You have 3 chances to make the right guess")
    hard()



