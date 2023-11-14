# Import the necessary libraries.
import Adafruit_CharLCD as LCD
import time


# Save data about the LCD screen.
LCD_COLUMNS = 16
LCD_ROWS = 2


# Initialize the LCD screen.
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)
lcd.set_backlight(0)

# Prompt the user for their name.
name = input("What is your name?")

# Say hello to the user on the LCD screen.
lcd.message('Hello\n' + name)
time.sleep(5)
lcd.clear()
lcd.set_backlight(1)
