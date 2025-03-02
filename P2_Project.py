# Caleb Caten, Dakota Dowd, Isaac Pratte, Josh Knight Lincoln Adams
# Plays the women's soccer season from Assignment 4 using imported custom functions

# Importing custom functions
from Introduction_Function import playerIntro
from josh_funct5 import displayRecord
from Caleb_menu_function import menu
from function4 import playGame
from teamlist import gameSelect

# Welcome: Requests the user's name and displays an introductory message
print()
sName = input("What is your name?: ")
sName = playerIntro(sName)

# Initializing variables
iOption = 0
iWins = 0
iLosses = 0
sHomeTeam = None
sAwayTeam = None

# Displaying menu and prompting for user input
iOption = menu()

# While loop to keep the program running until the user chooses to exit
# If statements to determine what the user wants to do
while iOption != 4 :

    if iOption == 1 : # Display list of teams, select home team, and select away team

        if sHomeTeam is None : # If statement to check if home team has been selected, if not, select home team
            sHomeTeam, sAwayTeam = gameSelect()
        else :
            _, sAwayTeam = gameSelect(sHomeTeam) # Otherwise only selects away team

    elif iOption == 2 :

        bOutcome = playGame(sHomeTeam, sAwayTeam) # Call the function to play the game

        if bOutcome == True : # If statement to keep track of wins and losses
            iWins = iWins + 1
        if bOutcome == False :
            iLosses = iLosses + 1

    elif iOption == 3 : # Display the final record
        displayRecord(iWins, iLosses, sHomeTeam)

    else :
        print("Exiting the game, see you next time!") # Exit the program

    iOption = menu() # Display the menu again