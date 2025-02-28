# Dakota Dowd IS303 Function
# Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message. 
# Return the name to the main program and store it in variable so it can be used throughout the program.


# Defining Player function
def Player(sName):
    # Displaying the introduction to the game
    print("\nHello " + str(sName) + "!")
    print("\nWelcome to the Soccer Tournament! \n\nThis is a game to generate random scores for a women's soccer tournament. \n\nPlease enter information as you are prompted, and we will discover the results of the tournament together!")
    return (sName)

