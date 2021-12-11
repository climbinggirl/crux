#Dice Game
import random
import time

roll_again = "yes"

while roll_again  == "yes" or roll_again == "y":
  #delay
  print("Rolling the dice...")
  time.sleep(3)
  #creating random number
  dice = random.randint(1,6)
  print("You rolled", dice)
  #ask to roll again
  print("Do you wanna roll again? (yes,y)")
  roll_again = input("> ")

print("You ended the game!")
