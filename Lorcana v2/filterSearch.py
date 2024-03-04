# Filter Search
import re

# Creating an empty dictionary
masterInput_dict = {}

# Filter 1
def inkColorFilter():
    inkColor = ['Amber','Amethyst','Emerald','Ruby','Sapphire','Steel']
    print(" == Ink Color: 1. Amber, 2. Amethyst, 3. Emerald, 4. Ruby, 5. Sapphire, 6. Steel")
    inkColor_input = input(" == Enter all the numbers to include (seperated by a comma): ")
    
    # Error Checking
    while re.search("^[^123456]",inkColor_input):
        print("Not an option. Please try again.")
        inkColor_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Splits list and turn into integers
    userInput_list = inkColor_input.split(',')
    int_numbers = [int(num_str) for num_str in userInput_list]

    # Translate userInput integers into color names
    for i in int_numbers:
        userInput_list.pop(0)
        userInput_list.append(inkColor[i-1])

    # Adding to masterInput
    if masterInput_dict.get('inkColor') is not None:
        currentList = masterInput_dict['inkColor'] # Finds list already existing in dictionary
        combinedList = [*currentList, *userInput_list] # Combining both lists
        masterInput_dict['inkColor'] = set(combinedList) # Removing duplicates and adding updated list to dictionary
    else:
        additional_data = {'inkColor': set(userInput_list)} # Checks and removes duplicates
        masterInput_dict.update(additional_data) # Adds list to dictionary if list does not exist yet

# Filter 2
def inkCostFilter():
    print(" == Ink Cost: 1 - 9")
    inkCost_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Error Checking
    while re.search("^[^123456789]",inkCost_input):
        print("Not an option. Please try again.")
        inkCost_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Splits list and turn into integers
    userInput_list = inkCost_input.split(',')
    int_numbers = [int(num_str) for num_str in userInput_list]

    # Adding to masterInput
    if masterInput_dict.get('inkCost') is not None:
        currentList = masterInput_dict['inkCost']
        combinedList = [*currentList, *int_numbers]
        masterInput_dict['inkCost'] = set(combinedList)
    else:
        additional_data = {'inkCost': set(int_numbers)}
        masterInput_dict.update(additional_data)
    
# Filter 3
def cardTypeFilter():
    cardType = ['%Action%', '%Song%', 'Character', 'Item']
    print(" == Card Type: 1. Action, 2. Song, 3. Character, 4. Item")
    cardType_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Error Checking
    while re.search("^[^1-4]",cardType_input):
        print("Not an option. Please try again.")
        cardType_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Splits list and turn into integers
    userInput_list = cardType_input.split(',')
    int_numbers = [int(num_str) for num_str in userInput_list]

    # Translate userInput integers into card type names
    for i in int_numbers:
        userInput_list.pop(0)
        userInput_list.append(cardType[i-1])

    # Adding to masterInput
    if masterInput_dict.get('cardType') is not None:
        currentList = masterInput_dict['cardType']
        combinedList = [*currentList, *userInput_list]
        masterInput_dict['cardType'] = set(combinedList)
    else:
        additional_data = {'cardType': set(userInput_list)}
        masterInput_dict.update(additional_data)

# Filter 4
def inkAbleFilter():
    print(" == Inkwell: 1. Yes, 2. No")
    inkAble_input = int(input(" == Enter either 1 or 2: "))

    # Error Checking
    while re.search("^[^1-2]",str(inkAble_input)):
        print("Not an option. Please try again.")
        inkAble_input = int(input(" == Enter either 1 or 2: "))
    
    # Assign input to Inkwell = 1, No Inkwell = 0
    if inkAble_input == 1:
        inkAble_input = 1
    elif inkAble_input == 2:
        inkAble_input = 0
    else:
        print("Invalid answer")

    # Adding to masterInput
    if masterInput_dict.get('inkAble') is not None:
        currentList = masterInput_dict['inkAble']
        combinedList = [*currentList, *(str(inkAble_input))]
        masterInput_dict['inkAble'] = set(combinedList)
    else:
        additional_data = {'inkAble': inkAble_input}
        masterInput_dict.update(additional_data)

# Filter 5
def charClassFilter():
    charClass = ['%Alien%','%Broom%','%Captain%','%Deity%','%Detective%','%Dragon%','%Fairy%','%Inventor%','%King%','%Knight%','%Musketeer%','%Pirate%','%Prince%','%Princess%','%Queen%','%Seven Dwarfs%','%Sorcerer%','%Tigger%']
    print(" == Classification: 1. Alien, 2. Broom, 3. Captain, 4. Deity, 5. Detective, 6. Dragon, 7. Fairy, 8. Inventor, 9. King, 10. Knight, 11. Musketeer, 12. Pirate, 13. Prince, 14. Princess, 15. Queen, 16. Seven Dwarfs, 17. Sorcerer, 18. Tigger")
    charClass_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Error Checking
    while re.search("^[^1-9]|\b1[0-9]]",charClass_input):
        print("Not an option. Please try again.")
        charClass_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Splits list and turn into integers
    userInput_list = charClass_input.split(',')
    int_numbers = [int(num_str) for num_str in userInput_list]

    # Translate userInput integers into classification names
    for i in int_numbers:
        userInput_list.pop(0)
        userInput_list.append(charClass[i-1])

    # Adding to masterInput
    if masterInput_dict.get('charClass') is not None:
        currentList = masterInput_dict['charClass']
        combinedList = [*currentList, *userInput_list]
        masterInput_dict['charClass'] = set(combinedList)
    else:
        additional_data = {'charClass': set(userInput_list)}
        masterInput_dict.update(additional_data)

# Filter 6
def cardRarityFilter():
    cardRarity = ['Common', 'Uncommon', 'Rare', 'Super Rare', 'Legendary']
    print(" == Rarity: 1. Common, 2. Uncommon, 3. Rare, 4. Super Rare, 5. Legendary")
    cardRarity_input = input(" == Enter all the numbers to include (seperated by a comma): ")
    
    # Error Checking
    while re.search("^[^1-5]",cardRarity_input):
        print("Not an option. Please try again.")
        cardRarity_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Splits list and turn into integers
    userInput_list = cardRarity_input.split(',')
    int_numbers = [int(num_str) for num_str in userInput_list]

    # Translate userInput integers into rarity names
    for i in int_numbers:
        userInput_list.pop(0)
        userInput_list.append(cardRarity[i-1])

    # Adding to masterInput
    if masterInput_dict.get('cardRarity') is not None:
        currentList = masterInput_dict['cardRarity']
        combinedList = [*currentList, *userInput_list]
        masterInput_dict['cardRarity'] = set(combinedList)
    else:
        additional_data = {'cardRarity': set(userInput_list)}
        masterInput_dict.update(additional_data)

# Filter 7
def charAbilityFilter():
    charAbility = ['%Bodyguard%', '%Evasive%', '%Resist%', '%Shift%', '%Support%','%Challenger%','%Reckless%','%Rush%','%Singer%','%Ward%']
    print(" == Keywords: 1. Bodyguard, 2. Evasive, 3. Resist, 4. Shift, 5. Support, 6. Challenger, 7. Reckless, 8. Rush, 9. Singer, 10. Ward")
    charAbility_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Error Checking
    while re.search("^[^1-9]|10]",charAbility_input):
        print("Not an option. Please try again.")
        charAbility_input = input(" == Enter all the numbers to include (seperated by a comma): ")

    # Splits list and turn into integers
    userInput_list = charAbility_input.split(',')
    int_numbers = [int(num_str) for num_str in userInput_list] 

    # Translate userInput integers into ability names
    for i in int_numbers:
        userInput_list.pop(0)
        userInput_list.append(charAbility[i-1])

    # Adding to masterInput
    if masterInput_dict.get('charAbility') is not None:
        currentList = masterInput_dict['charAbility']
        combinedList = [*currentList, *userInput_list]
        masterInput_dict['charAbility'] = set(combinedList)
    else:
        additional_data = {'charAbility': set(userInput_list)}
        masterInput_dict.update(additional_data)

# Error checking
def default():
    print("==============================================================")
    print("1. Ink color: Amber, Amethyst, Emerald, Ruby, Sapphire, Steel")
    print("2. Ink cost: 1-9")
    print("3. Card type: Action, Song, Character, Item")
    print("4. Inkwell: Yes/No")
    print("5. Classifications: Alien, Broom, Captain, Deity, Detective, Dragon, Fairy, Inventor, King, Knight, Musketeer, Pirate, Prince, Princess, Queen, Seven Dwarfs, Sorcerer, Tigger")
    print("6. Rarity: Common, Uncommon, Rare, Super Rare, Legendary")
    print("7. Keywords: Bodyguard, Evasive, Resist, Shift, Support, Challenger, Reckless, Rush, Singer, Ward")
    print("==============================================================")
    userFilterNum = int(input("Enter number of filter (1-7): "))
    filter_switch_case(userFilterNum)

# Switch case for the Filter Selection page
def filter_switch_case(case):
    filter_switch_dict = {
        1: inkColorFilter,
        2: inkCostFilter,
        3: cardTypeFilter,
        4: inkAbleFilter,
        5: charClassFilter,
        6: cardRarityFilter,
        7: charAbilityFilter,
    }

    case_function = filter_switch_dict.get(case, default)
    case_function()