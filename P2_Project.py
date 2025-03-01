# Caleb Caten, Dakota Dowd, Isaac Pratte, Josh Knight Lincoln Adams

# Imports Custom Functions
from Introduction_Function import Player
from josh_funct5 import displayRecord
from Caleb_menu_function import menu
from function4 import playGame

# Welcome: Requests the user's name and displays an introductory message
sName = input("What is your name? ")
sName = Player(sName)

option = 0
wins = 0
losses = 0
menu()

if option == 1 :
    #function 3

if option == 2 :
    bOutcome = playGame()

    #create an if statement to keep track of wins and losses
    if bOutcome == True :
        wins = wins + 1
    if bOutcome == False :
        losses = losses + 1

if option == 3 :
    displayRecord(wins, losses, sHomeTeam)

if option == 4 :
    print("Exiting the game, see you next time!")