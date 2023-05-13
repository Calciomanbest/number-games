import random

random_number=random.randint(1,100)
guesses = 0


while True:
    user_guess =int(input("Guess a number between 1 and 100: "))
    guesses += 1

    if user_guess > random_number:
        print("Too high")
    elif user_guess< random_number:
        print("too low")
    else:
        print(f"correct you guessed the number in {guesses}")
        break
