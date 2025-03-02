# Display list of all teams and allow the user to choose a team using a menu. 
# Call the function again to let the user choose the opponent but do not display the team they chose previously. 
# Remove that team from the list. Allow the user to select an opponent, and return team name. 
# This function should receive a parameter but give it a default value if none is passed. 
# You can use this function for both choosing the home team and the opponent team.

def gameSelect(lstTeams = None) :
    if lstTeams is None:
        lstTeams = [
            "BYU",
            "TCU",
            "Texas Tech",
            "West Virginia",
            "Oklahoma State",
            "Kansas",
            "Arizona",
            "Utah",
            "Colorado",
            "Baylor",
            "Arizona State",
            "Cincinnati",
            "UCF",
            "Iowa State",
            "Houston",
            "Kansas State"
        ]

    def printList() :

        iTeamNumber = 1
        for iCount in lstTeams:
            print(f"{iTeamNumber} : {iCount}\n")
            iTeamNumber += 1
    
    # Select home team
    while True:
        printList()
        try:
            iTeamSelect = int(input('Please select the home team by typing its number (Example: "3"): '))
            if iTeamSelect < 1 or iTeamSelect > len(lstTeams):
                print("Invalid selection. Please choose a valid team number.")
            else:
                sHomeTeam = lstTeams.pop(iTeamSelect - 1)
                print(f"\nAs the home team, you have selected {sHomeTeam}.\n")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Select away team
    while True:
        printList()
        try:
            iTeamSelect = int(input('Please select the away team by typing its number (Example: "3"): '))
            if iTeamSelect < 1 or iTeamSelect > len(lstTeams):
                print("Invalid selection. Please choose a valid team number.")
            else:
                sAwayTeam = lstTeams.pop(iTeamSelect - 1)
                print(f"\nAs the away team, you have selected {sAwayTeam}.\n")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    return sHomeTeam, sAwayTeam
