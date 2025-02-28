# Caleb Caten section 004 group 5

# Define menu funciton
def menu() :
    option = 0

    # Use a while loop to cycle through options
    while option != 4 :        
        print("     Menu: \n  1. Show list of teams. \n  2. Play the game. \n  3. Display the final record. \n  4. Exit program.")

        # Try-except to only allow input of 1-4
        try :
            option = int( input("Please choose an option.  "))
            if option not in [1, 2, 3, 4] :
                print("Sorry, please enter a number between 1 and 4. ")
        except ValueError :
            print("Sorry, you need to type a whole number between 1 and 4.")
            continue
    return option
