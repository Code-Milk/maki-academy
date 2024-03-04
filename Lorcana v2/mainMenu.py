# Main Menu
from filterMenu import filterPrompt, catalogSearch
from loreCounter import *
import sqlite3

# Prompts menu for user
def menuPrompt():
    print("\nMain menu:")
    print("1 - Catalog Search")
    print("2 - Lore Counter")
    print("3 - Game Rules")
    print("4 - Exit\n")

    userInput = int(input("Enter the number of what you'd like to do: "))
    menu_switch_case(userInput)

# Displays game rules
def gameRules():
    with open('gameRules.txt','r') as file:
        file_contents = file.read()
        print(file_contents)

def exitLibrary():
    print("Thank you for using the Lorcana Library!")
    exit()

# Error for incorrect option / Default
def default():
    print("This is not an option. Please try again.\n")
    userInput = int(input("Enter the number of what you'd like to do: "))
    menu_switch_case(userInput)

# Switch case function for Main Menu page
def menu_switch_case(case):
    menu_switch_dict = {
        1: catalogSearch,
        2: loreCounter,
        3: gameRules,
        4: exitLibrary
    }

    case_function = menu_switch_dict.get(case, default)
    case_function()
    menuPrompt()

# Welcome user and prompts menu
print("================================")
print("Welcome to the Lorcana Database!")
print("================================")
menuPrompt()