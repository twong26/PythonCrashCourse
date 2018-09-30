# five places i want to visit
locations = ['pyramids', 'bali', 'patagonia', 'dolomites', 'girona']

# print list in original order/raw python list
print(locations)

# use sorted() to print your list in alpha order w/o modifying the actual list
print(sorted(locations))

# show that your list is still in its original order by printing it
print(locations)

# use sorted() to print your list in reverse alpha order without changing
# the order of the list
print(sorted(locations, reverse=True)) # had to look this one up online

# show that your list is still in its original order by printing it again
print (locations)

# Use reverse to change the order of your list. 
# Print the list to show that its order has changed.

locations.reverse()
print(locations)

## why didn't print(locations.reverse()) work? it returned None. I guess it's
## because it's a list? I tried to make it a string and it still didn't print.
## You can't convert a list to a string?

# use reverse() to change the orer of your list again. Print the list to show it's back to its orgiinal order

locations.reverse()
print(locations)

# use sort() to change your list so it's sorted in alpha order. print the list to shwo that its order has been changed

locations.sort()
print(locations)

# use sort() to change your list so it's sorted in reverse alphabetical order. Print the list to show that its order has changed

locations.sort(reverse=True)
print(locations)