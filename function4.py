# Isaac Pratte | IS 303 | Section 004 | Group 5
# Play the game receiving both team names. Generate random scores without ties. Return W or L.

import random

def playGame(sHomeTeam, sAwayTeam):

    iHomeScore = random.randrange(0,10)
    iAwayScore = random.randrange(0,10)
    
    # Prevent ties
    while iAwayScore == iHomeScore :
        iHomeScore = random.randrange(0,10)

    # Convert scores to string
    sHomeScore = str(iHomeScore)
    sAwayScore = str(iAwayScore)

    print("Final score: " + sHomeTeam + ": " + sHomeScore + ". " + sAwayTeam + ": " + sAwayScore + ".")

    return "W" if iHomeScore > iAwayScore else "L"