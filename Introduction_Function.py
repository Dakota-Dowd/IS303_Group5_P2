# Dakota Dowd IS303 Function
# Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message. 
# Return the name to the main program and store it in variable so it can be used throughout the program.

# Defining function
def playerIntro(sName):
    # Displaying the introduction to the game
    print("\nHello " + str(sName) + "!")
    print("\nWelcome to the NCAA Women's Soccer Tournament! \n\nThis is a game to generate random scores for a women's soccer tournament. \n\nFirst, we will ask you the name of the home team, as well as how many games that team will play.")
    print("\nThen, based on how many games are played, you will be asked to name opposing teams. \n\nIn the end, we will generate scores and show you how well your team did during the season! Let's go!")
    print("-" * 100)
    print("\n\n")
    return (sName)

