# Write code below 💖

# Task 1: Create Player Data
captains = [
  {'name': 'Daichi Sawamura','position': 'Wing Spiker','weight': '70.1kg','spikes': 20},
  {'name': 'Bokuto Koutarou','position': 'Wing Spiker','weight': '78.3kg','spikes': 56},
  {'name': 'Kuroo Tetsurou','position': 'Middle Blocker','weight': '75.3kg','spikes': 8},
  {'name': 'Oikawa Tohru','position': 'Setter','weight': '72.2kg','spikes': 5}
]

print("Player Names:")
for player in captains:
  print(player['name'])

# Task 2: Analyze Player Positions
print("\nPlayer Positions:")
for player in captains:
  print(player['position'])

# Task 3: Update Player Statistics
print("\nPlayer Spike Count: ")
captains[2]['spikes'] += 10
print(captains[2]['name'], ": ",captains[2]['spikes'])

# Task 4: Calculate Average
total_spikes = 0
for player in captains:
  total_spikes += player['spikes']
avg_spikes = total_spikes/len(captains)
print("\nAverage Spikes: ", avg_spikes)