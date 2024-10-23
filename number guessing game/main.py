import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("I have selected a number between 1 and 100. Can you guess it?")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")

guess_the_number()
