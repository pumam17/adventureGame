# -----------------------------------------------------------------
# Project Name: adventure game 
# Name: Mitch Puma
# -----------------------------------------------------------------
import random
import time
# -----------------------------------------------------------------
# Function Name:        Validate_Integer_Input
# Function Purpose:     Validate any integer data
# -----------------------------------------------------------------
def Validate_Integer_Input(intInput):
   try:
        intInput = int(intInput)
        if(intInput == 0 or intInput == 1):
            global strValidated
            strValidated = True
        else:
            print("Input must be 0 or 1")
   except ValueError:
        intInput = int(0)
        print("Input must be 0 or 1")
   return intInput

# -----------------------------------------------------------------
# Function Name:        Display_Menu
# Function Purpose:     Display game menu and instructions
# -----------------------------------------------------------------
def Display_Menu():
    print("Choose you own adventure game.")
    print("Enter 0 for no. Enter 1 for yes.")
    print("--------------------------------")
    return

# -----------------------------------------------------------------
# Function Name:        Challenge_Number_One
# Function Purpose:     Choose the correct path 
# -----------------------------------------------------------------
def Challenge_Number_One(intUserInput):
    intRandomNumber = int(0)
    intDeath = int(0)

    intRandomNumber = random.randint(0, 1)
    if (intRandomNumber == intUserInput):
        print("You answered correctly. The stranger warns you of the ambush. You arrive at your destination unharmed.")
        intDeath = 1
    else:
        print("You did not survie the test.")
       
    return intDeath

# -----------------------------------------------------------------
# Function Name:        Challenge_Number_Two
# Function Purpose:     Choose the correct path 
# -----------------------------------------------------------------
def Challenge_Number_Two(intUserInput):
    intUserDamage = random.randint(1, 100)
    strUserDamage = str(intUserDamage)
    if (intUserInput == 0):
        print("You block the opponent. He does not want to fight you anymore and runs away.")
    else:
        print("You attack the opponent. If your attack damage is greater than zero you win.")

        print("User damage: " + "\u001b[31m" + strUserDamage)

    return



# -----------------------------------------------------------------
# Name:                 Controlling Main Code for Applications
# Purpose:              Controls the flow for Application
# -----------------------------------------------------------------

intAnotherUser = 1
strValidated = bool(False)
intDeath = int(0)
sngStartTime = float(0)
sngStopTime = float(0)
sngFinalTime = float(0)
Display_Menu()
while intAnotherUser == 1:

    print("\nA stranger asks you a simple question is your response yes or no?.")


    while strValidated is False:
        intUserInput = input()
        intUserInput = Validate_Integer_Input(intUserInput)
    strValidated = bool(False)

    intDeath = Challenge_Number_One(intUserInput)

    if(intDeath == 1):

        print("\nYou arrive at your second challenge. You are attacked by an enemy.")
        
        sngStartTime = time.time()

        while strValidated is False:
            intUserInput = input("Will you attack the opponent?\n")
            intUserInput = Validate_Integer_Input(intUserInput)
        strValidated = bool(False)

        sngStopTime = time.time()
        sngFinalTime = sngStopTime - sngStartTime

        if (sngFinalTime >= 31):
            intDeath = 0
        else:
            Challenge_Number_Two(intUserInput)


        if(intDeath == 1):

            print("\u001b[37m")
            print("You won congratulations. Try again?")
            while strValidated is False:
                intAnotherUser = input("Enter 0 to exit. Enter 1 to continue.\n")
                intAnotherUser = Validate_Integer_Input(intAnotherUser)
            strValidated = bool(False)
        else:
            print("You lost because you took to long. Try again?")
            while strValidated is False:
                intAnotherUser = input("Enter 0 to exit. Enter 1 to continue.\n")
                intAnotherUser = Validate_Integer_Input(intAnotherUser)
            strValidated = bool(False)
    else:
        print("You lost because you died. Try again?")
        while strValidated is False:
            intAnotherUser = input("Enter 0 to exit. Enter 1 to continue.\n")
            intAnotherUser = Validate_Integer_Input(intAnotherUser)
        strValidated = bool(False)
    

