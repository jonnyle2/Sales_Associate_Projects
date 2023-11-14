# Import appropriate libraries.
import random


# Prompt the user for their name and say hello.
name = input("Hello! What is your name?\n")
print("Hello there " + name + "! I am thinking of a number between 1 and 100.")

# Prepare the game's variables.
my_number = random.randint(1, 100)
guess_history = []

# Begin the guessing loop with 10 tries.
for guess_count in range(1, 11):
    # Prompt the user for a number.
    valid_guess = False
    while not valid_guess:
        # Validate user input.
        try:
            number_guessed = int(input("Take a guess...\n"))
            valid_guess = True
        except ValueError:
            # The user didn't give us a number!
            print("Please provide a valid number.")

    # Find out how close the user was to the real number.
    guess_difference = abs(my_number - number_guessed)

    # Add this guess to the guess history list.
    guess_history.append(number_guessed)

    # Check how close the guess is.
    if number_guessed < my_number and guess_difference > 10:
        print("Your guess is very low. Try again.")
    elif number_guessed > my_number and guess_difference > 10:
        print("Your guess is very high. Try again.")
    elif number_guessed < my_number and guess_difference < 10:
        print("You're close, but your guess is too low. Try again.")
    elif number_guessed > my_number and guess_difference < 10:
        print("You're close, but your guess is too high. Try again.")
    else:
        # They guessed the number correctly!
        break

# Check if a correct guess was made.
if number_guessed == my_number:
    print("Great job " + name + "! You guessed my number in " + str(guess_count) + " guesses.")
    print("Your guesses were: " + " ".join(str(i) for i in guess_history))
else:
    print("Sorry! You didn't guess my number. The number I am thinking of is " + str(my_number) + ".")
    