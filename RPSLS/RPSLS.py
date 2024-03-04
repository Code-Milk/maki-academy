# Rock, Paper, Scissors, Lizard, Spock
import random

choice = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock', 1, 2, 3, 4, 5]

# Start game
print("\n=====================================")
print("Rock, Paper, Scissors, Lizard, Spock!")
print("=====================================\n")
print("1) Rock")
print("2) Paper")
print("3) Scissors")
print("4) Lizard")
print("5) Spock\n")

# Player selection
player = int(input("Select a number between 1 and 5: "))

# Computer random
cpu = random.randint(1,5)

# Error checking
while player not in choice:
    player = int(input("Error! Pick another number: "))

# Player choices
print("======================")
print(f"You chose: {choice[player - 1]}")
print(f"CPU chose: {choice[cpu - 1]}")

# Winning =====
# Draw =====
if player == cpu:
    print("Draw!")
elif (player == 3) and (cpu == 2 or cpu == 4):
    print("You win!")
    # Scissors cut Paper = 3 > 2
    # Scissors beat Lizard = 3 > 4
elif (player == 1) and (cpu == 4 or cpu == 3):
    print("You win!")
    # Rock crushes Lizard = 1 > 4
    # Rock breaks Scissors = 1 > 3
elif (player == 4) and (cpu == 5 or cpu == 2):
    print("You win!")
    # Lizard poisons Spock = 4 > 5
    # Lizard eats Paper = 4 > 2
elif (player == 2) and (cpu == 5 or cpu == 1):
    print("You win!")
    # Paper disproves Spock = 2 > 5
    # Paper covers Rock = 2 > 1
elif (player == 5) and (cpu == 1 or cpu == 3):
    print("You win!")
    # Spock vaporizes Rock = 5 > 1
    # Spock smashes Scissors = 5 > 3
# Losing =====
else:
    print("You lose!")

print("======================")