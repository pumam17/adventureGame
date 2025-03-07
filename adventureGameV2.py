# -----------------------------------------------------------------
# Project Name: adventure game 
# Name: Mitch Puma
# -----------------------------------------------------------------
import random
import time



# -----------------------------------------------------------------
# Function Name:        Validate_UserInput
# Function Purpose:     Validate integer data
# -----------------------------------------------------------------
def Validate_UserInput(intValidation):

   while intValidation == INT_BOOLEAN_FALSE:
       try:
            intUserInput = int(input())
            if(intUserInput == 0 or intUserInput == 1):
                intValidation = INT_BOOLEAN_TRUE
            else:
                print("Input must be 0 or 1")
       except ValueError:
            intInput = int(0)
            print("Input must be 0 or 1")
   intValidation = INT_BOOLEAN_FALSE
   return intUserInput



# -----------------------------------------------------------------
# Function Name:        Display_Menu
# Function Purpose:     Display game menu and instructions
# -----------------------------------------------------------------
def Display_Menu(strGameMessage):
    print("\u001b[37m" + strGameMessage)
    print("Enter 0 for no. Enter 1 for yes.")
    print("--------------------------------")
    return



# -----------------------------------------------------------------
# Function Name:        
# Function Purpose:     
# -----------------------------------------------------------------
def Calculate_Time(sngStartTime):
    sngStopTime = time.time()
    sngFinalTime = sngStopTime - sngStartTime
    if (sngFinalTime >= INT_TIME_LIMIT):
        intDeath = INT_BOOLEAN_TRUE
        sngFinalTime = round(sngFinalTime, 2)
        print("Player phase took to long you died. ", sngFinalTime)
    else:
        intDeath = INT_BOOLEAN_FALSE
        sngFinalTime = round(sngFinalTime, 2)
        strFinalTime = str(sngFinalTime)
        print("Player phase was " + strFinalTime + "s")
    return intDeath



# -----------------------------------------------------------------
# Name:                 Dice_Roll
# Purpose:              Return a random value
# -----------------------------------------------------------------
def Dice_Roll():
    intDiceRoll = random.randint(1, 6)
    strDiceRoll = str(intDiceRoll)
    print("Your dice roll was: " + "\u001b[31m" + strDiceRoll)
    return intDiceRoll


# -----------------------------------------------------------------
# Name:                 Controlling Main Code for Applications
# Purpose:              Controls the flow for Application
# -----------------------------------------------------------------

INT_BOOLEAN_TRUE = int(1)
INT_BOOLEAN_FALSE = int(0)
INT_USERINPUT_YES = int(1)
INT_USERINPUT_NO = int(0)
INT_TIME_LIMIT = int(31)

sngStartTime = float(0)
sngStopTime = float(0)
sngFinalTime = float(0)

intDiceRoll = int(0)

intValidation = INT_BOOLEAN_FALSE

strGameMessage = "Choose you own adventure game. Would you like to play?"
Display_Menu(strGameMessage)

intAnotherUser = Validate_UserInput(intValidation)

while intAnotherUser == 1:

    intDiceRoll = Dice_Roll()
    strGameMessage = "You reach a bridge do you cross the bridge?"
    Display_Menu(strGameMessage)
    sngStartTime = time.time()
    intUserInput = Validate_UserInput(intValidation)
    intDeath = Calculate_Time(sngStartTime)

    if (intDeath == INT_BOOLEAN_FALSE):

        if (intUserInput == INT_USERINPUT_YES):
            if(intDiceRoll % 2 == 0):
                print("\u001b[37m" + "The bridge was evenly constructed. You made it across safe.")
            else:
                print("\u001b[37m" + "The bridge was oddly constructed. You did not make it across safe.")
                intDeath = INT_BOOLEAN_TRUE 

        if (intUserInput == INT_USERINPUT_NO):
            if (intDiceRoll > 3):
                print("\u001b[37m" + "You did not cross the bridge so you are safe.")
            else:
                print("\u001b[37m" + "You did not cross the bridge so you are safe, but you were attacked by a monster.")
                intDeath = INT_BOOLEAN_TRUE 

        if (intDeath == INT_BOOLEAN_FALSE):
            print("You Win")
        else:
            print("You Lose")

    else:
        print("You Lose")

    strGameMessage = "Choose you own adventure game. Would you like to play?"
    Display_Menu(strGameMessage)

    intAnotherUser = Validate_UserInput(intValidation)

