# Lore Counter

def loreCounter():
    print("==============================================================")
    print("Welcome! This is the Lore Counter to keep track of your score during your game.\n")

    loreTracker = {} # Create empty dictionary for counter

    # Input number of players
    playerCount = int(input("Enter the number of players (2 or more): "))
    while playerCount < 2:
        print("Needs 2 or more players. Try again!")
        playerCount = int(input("Enter the number of players (2 or more): "))
    
    print(f' == There will be {playerCount} players in the game. Everyone starts with 0 lore.\n')
    
    # Adding players to dictionary
    for i in range(playerCount):
        playerNum = 'Player ' + str(i + 1) # Creating each unique player
        playerInput = {playerNum: 0} # Assigning score of 0 to each player
        loreTracker.update(playerInput) # Update Lore Tracker dictionary

    print("Start game. Good luck!")

    winTracker = False
    while winTracker is False:
        # Print current score
        print("================ Current Score ================")
        for player, score in loreTracker.items():
            print(f" == {player}: {score}")
        print("===============================================")

        # Prompt to update score
        playerInput = input("Enter Player Number to edit Lore: ")
        # Error checking
        while (int(playerInput) > playerCount) or (int(playerInput) < 1):
            print("That player does not exist. Please try again.")
            playerInput = input("Enter Player Number to edit Lore: ")
        scoreInput = int(input("Input lore (insert a negative if taking away lore): "))

        # Update score to player
        playerNum = 'Player ' + str(playerInput)
        loreTracker[playerNum] += scoreInput

        # Score can't go below 0
        if loreTracker.get(playerNum) < 0:
            playerNum = 'Player ' + str(playerInput)
            loreTracker[playerNum] = 0

        # Player wins once they get to 20 or higher
        if loreTracker.get(playerNum) > 19:
            print("==================== Winner ====================")
            print(f"{playerNum} won the game with {loreTracker.get(playerNum)} lore! Congrats!")
            print("=================== End Game ===================")
            winTracker = True # End game

    #menuPrompt()