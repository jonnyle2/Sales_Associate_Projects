# Import appropriate libraries.
import time
import random
from rpi_ws281x import PixelStrip, Color
from Adafruit_LED_Backpack import SevenSegment

LED_COUNT = 64        # Number of LED pixels.
LED_PIN = 12          # GPIO pin connected to the pixels
LED_FREQ_HZ = 800000  # LED signal frequency in hertz
LED_DMA = 10          # DMA channel to use for generating signal
LED_BRIGHTNESS = 10   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Prompt the user for their name and say hello.
name = input("Hello! What is your name?\n")
print("Hello there " + name + "! I am thinking of a number between 1 and 100.")

# Prepare the game's variables.
my_number = random.randint(1, 100)
guess_history = []

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def colorAll(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()


segment = SevenSegment.SevenSegment(address=0x70)
# Initialize the display. Must be called once before using the display.
segment.begin()
segment.set_digit(3, 0)
segment.set_digit(2, 1)
segment.write_display()
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
        colorAll(strip, Color(255, 0, 0))
        print("Your guess is very low. Try again.")
    elif number_guessed > my_number and guess_difference > 10:
        colorAll(strip, Color(255, 0, 0))
        print("Your guess is very high. Try again.")
    elif number_guessed < my_number and guess_difference <= 10:
        colorAll(strip, Color(255, 0, 0))
        print("You're close, but your guess is too low. Try again.")
    elif number_guessed > my_number and guess_difference <= 10:
        colorAll(strip, Color(255, 0, 0))
        print("You're close, but your guess is too high. Try again.")
    else:
        # They guessed the number correctly!
        break
    segment.clear()
    segment.set_digit(3, 10 - guess_count)
    segment.write_display()

# Check if a correct guess was made.
if number_guessed == my_number:
    colorAll(strip, Color(0, 255, 0))  # Green wipe
    print("Great job " + name + "! You guessed my number in " + str(guess_count) + " guesses.")
    print("Your guesses were: " + " ".join(str(i) for i in guess_history))
    time.sleep(3)
    colorAll(strip, Color(0, 0, 0))
    segment.clear()
    segment.write_display()
else:
    print("Sorry! You didn't guess my number. The number I am thinking of is " + str(my_number) + ".")
    time.sleep(3)
    colorAll(strip, Color(0, 0, 0))
    segment.clear()
    segment.write_display()
