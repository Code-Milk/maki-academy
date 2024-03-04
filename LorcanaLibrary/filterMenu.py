# Filter Selection Page
from filterSearch import *
import sqlite3

# Prints all cards
def catalogSearch():
    # Opens connection
    conn = sqlite3.connect('lorcanadb.db')
    cur = conn.cursor()
    
    # Run SQL Query
    card_data = cur.execute("SELECT cardName,inkColor,inkCost,cardType,inkAble,charClass,cardRarity,charAbility FROM lorcana") # Entire Catalog ordered by Card Num

    print("=============================== ENTIRE CATALOG ===============================")
    # Prints out the entire catalog row by row
    for row in card_data:
        print(row)

    # Closes connection
    cur.close()
    conn.close()
    
    filterPrompt() # Calls function to prompt user for filter selection

# Prompt user to add/remove filter
def filterPrompt():
    print("==============================================================")
    userInputFilter = input("Would you like to add a filter (Y/N)? ").lower()
    
    # Ends program if user does not want to add anything
    if (userInputFilter == 'n'):
        print("Thank you for using the Catalog Search.")
    # Prompt user to choose filter to begin
    elif (userInputFilter == "y"):
        while (userInputFilter == "y"): # Add multiple filters to dictionary 
            print("==============================================================")
            print("1. Ink color: Amber, Amethyst, Emerald, Ruby, Sapphire, Steel")
            print("2. Ink cost: 1-9")
            print("3. Card type: Action, Song, Character, Item")
            print("4. Inkwell: Yes/No")
            print("5. Classifications: Alien, Broom, Captain, Deity, Detective, Dragon, Fairy, Inventor, King, Knight, Musketeer, Pirate, Prince, Princess, Queen, Seven Dwarfs, Sorcerer, Tigger")
            print("6. Rarity: Common, Uncommon, Rare, Super Rare, Legendary")
            print("7. Keywords: Bodyguard, Evasive, Resist, Shift, Support, Challenger, Reckless, Rush, Singer, Ward")
            print("==============================================================")
            
            # Prompt user to select filter
            userFilterNum = int(input("Enter number of filter (1-7): "))
            # Error checking
            while (userFilterNum < 1) or (userFilterNum > 7):
                print("Not a valid number. Please try again.")
                userFilterNum = int(input("Enter number of filter (1-7): "))
            # Calls filter functions
            filter_switch_case(userFilterNum)
            print("==============================================================")

            # Keep prompting user to add to dictionary
            userInputFilter = input("Would you like to add another filter (Y/N)? ").lower()
            # Error checking
            while (userInputFilter != 'y') and (userInputFilter != 'n'):
                print("Not an option. Please try again.")
                userInputFilter = input("Would you like to add another filter (Y/N)? ").lower()
            if (userInputFilter == 'n'): # Stop adding to dictionary to start SQL query
                break

        print("==============================================================")
        print("Your Search Filter:")
        print(masterInput_dict) # Displays search dictionary
        
        # Call function to output User search results
        filterSQL()
    else:
        # Error checking
        print("Not an option. Please try again.")
        filterPrompt()
    
# SQL Search
def filterSQL():
    # Opens connection
    conn = sqlite3.connect('lorcanadb.db')
    cur = conn.cursor()

    # Create Query to find filter search
    SQLquery = "SELECT cardName,inkColor,inkCost,cardType,inkAble,charClass,cardRarity,charAbility FROM lorcana WHERE "
    # Cleaning format to work in SQL
    for key,values in masterInput_dict.items():
        SQLquery += "("
        if (key == 'charClass') or (key == 'charAbility'): # Due to LIKE, we want to include cards that includes these keywords separately
            for vals in values:
                SQLquery += key + " LIKE '" + str(vals).replace("[","").replace("]","").replace("{","").replace("}","") + "' OR "
            SQLquery = SQLquery[0:SQLquery.rindex('OR')] # Removing last OR from query
        else:
            SQLquery += key + " in (" + str(values).replace("[","").replace("]","").replace("{","").replace("}","") + ")"
        SQLquery += ")"
        SQLquery += ' AND '
    SQLquery = SQLquery[0:SQLquery.rindex('AND')] # Removing last AND from query

    print(SQLquery) # Displays the SQL Query
    card_data = cur.execute(SQLquery)

    # Print Catalog Search
    print("\n==============================================================")
    print("Results will show in this order:")
    print("(Card Name, Ink Color, Ink Cost, Card Type, Inkwell, Classification, Rarity, Ability)")
    print("==============================================================")
    # Displays each result by row
    for row in card_data:
        print(row)
    print("==============================================================\n")
    
    print("Thank you for using the Search Filter! The filter has been reset.")
    masterInput_dict.clear()

    # Closes connection
    cur.close()
    conn.close()