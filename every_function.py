candies = ['nibs', 'twizzlers', 'swedish berries', 'cola bottles']
print(candies)

# access elements in a list
print(candies[0])
print(candies[-1])

# using individual values from a list
message = "My favourite candy today is " + candies[0].title() + "."
print(message)

# modify elements in a list
## change the value of the first item - overwrite nibs with spk
candies[0] = 'sour patch kids'
print (candies)

# adding elements to a list

## appending elements to the end of a list - use append() method
## can use this to build list dynamically
candies.append('nibs')
print(candies)

## inserting elements into a list - use insert() method
candies.insert(0, 'chocolate')
print(candies)

# removing elements from a list
## removing an item using the del statement - if you know the position

del candies[1]
print(candies)

## remove an item using the pop() method
popped_candy = candies.pop()
print(candies)
print('The popped candy is ' + popped_candy.title() +".")

## popping items from any position in a list
first_eaten = candies.pop(0)
print('The first candy I ate today was ' + first_eaten.title() + '.')

## removing an item by value using remove() method
print(candies)
least_favourite = 'twizzlers'
candies.remove(least_favourite)
print("Let's remove my least favourite candy, which is " + least_favourite.title() + ".")

##########################


drinks = ['whiskey', 'rye', 'bourbon', 'vodka', 'rum', 'gin']

# sorting  list permanently with the sort() method - alpha order
drinks.sort()
print(drinks)

# sort list in reverse alpha by passing the argument to the sort method
drinks.sort(reverse=True)
print(drinks)

# let's go back to the original list.
print("\nHere is the original list:")
print(drinks)

# sorting a list temporarily with the sorted() function
print("\nHere is the sorted list:")
print(sorted(drinks))

print("\nHere's the original list again:")
print(drinks)

# reverse the order of the list
drinks.reverse()
print(drinks)

# now put it back
drinks.reverse()
print(drinks)

# finding the length of a list
print("The number of drinks is: " + str(len(drinks)))
print("The number of drinks is:" , len(drinks))

# find the middle of a list
middle_drink = int(len(drinks)/2)
print(middle_drink)
print("The middle drink is " + drinks[middle_drink])