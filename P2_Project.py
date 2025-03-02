# Caleb Caten, Dakota Dowd, Isaac Pratte, Josh Knight Lincoln Adams

# Imports Custom Functions
from Introduction_Function import Player
from josh_funct5 import displayRecord
from Caleb_menu_function import menu
from function4 import playGame
from teamlist import gameSelect

# Welcome: Requests the user's name and displays an introductory message
sName = input("What is your name? ")
sName = Player(sName)

iOption = 0
iWins = 0
iLosses = 0

iOption = menu()

while iOption != 4 :
    if iOption == 1 :
        sHomeTeam, sAwayTeam = gameSelect()
    elif iOption == 2 :
        bOutcome = playGame(sHomeTeam, sAwayTeam)

        #create an if statement to keep track of wins and losses
        if bOutcome == True :
            iWins = iWins + 1
        if bOutcome == False :
            iLosses = iLosses + 1
    elif iOption == 3 :
        displayRecord(iWins, iLosses, sHomeTeam)
    else :
        print("Exiting the game, see you next time!")

    iOption = menu()