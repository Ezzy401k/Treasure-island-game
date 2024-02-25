print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Tresure Islan Your mission is to find the treasure.")
# accept the player's input and assign it to the crossroads variable.
crossroad = input("Your at a crossroad. Where do you go? Type 'left' or'right'.\n")
# validate the player's choice.
if crossroad == "left":
          # accept the player's second choice.
    lake = input("You have come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for the boat or 'swim' to swim across the lake.\n")
          # validate the player's choice.
    if lake == "wait":
              # accept the player's third choice.
        house = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which door do you choose?\nred, yellow, blue.\n')
              # validate the player's choice.
        if house == "red":
            print("It's a room full of fire. Game Over.")
        elif house == "yellow":
            print("You found the treasure! You Win!")
        elif house == "blue":
            print("You entered room full of beastes. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You lost your stamina half way and drowned. Game Over.")
elif crossroad == "right":
    print("You fell in to a hole. Game Over.")
