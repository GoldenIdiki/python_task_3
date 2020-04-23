secret_number = 10
guess_chance = 0
guess_limit = 3
guess_option = list(range(1, 11))
print(guess_option)
print(type(guess_option))
print(guess_option[9])
y = False
while guess_chance < guess_limit:
    guess = int(input("Please make a guess: "))
    x = isinstance(guess, (float, str))
    print("go")
    if guess == secret_number:
        print("You won! You're a genius")
        break
    elif guess != secret_number:
        guess_chance += 1
else:
    print("Sorry try again later")


