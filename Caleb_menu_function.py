# Caleb Caten 
# Section 004 Group 5

# Define menu funciton
def menu() :
    iOption = 0
    while iOption not in [1, 2, 3, 4] :
    
        print("\n\n")    
        print("     Menu: \n  1. Show list of teams. \n  2. Play the game. \n  3. Display the final record. \n  4. Exit program.")

        try :
            iOption = int( input("Please choose an option.  "))
            if iOption not in [1, 2, 3, 4] :
                print("Sorry, please enter a number between 1 and 4. ")
        except ValueError :
            print("Sorry, you need to type a whole number between 1 and 4.")
    return iOption
