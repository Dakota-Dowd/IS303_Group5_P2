# Josh Knight IS 303 Section 004 Group 5
# Display the final record for a team.  Receive the home team data and display the information.

def displayRecord(Wins, Losses, TeamName) :
    
    #create a variable to hold the record.
    WinRatio = str(f"{Wins}-{Losses}")

    #print out the record
    print(f"The record for {TeamName} is {WinRatio}")