players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# if you want the second third, and fourth items in a list

print(players[1:4])

# if you omit the first index - auto start at beginning
print(players[:4])

# if you omit the last index - returns all items from the third item through the end
print(players[2:])

# specifying an index with only a colon gives a copy
print(players[:])

# output the last three players on roster
print(players[-3:])

# looping thru a slice
# loop thru first three players and print their name 
# as part of a simple roster

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())