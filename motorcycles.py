motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#removing a specific list item
#motorcycles.remove('ducati')
#print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# popping
# popped_motorcycle = motorcycles.pop() # pops off the last item off the top of the stack
# print(motorcycles) # remaining list does not include the popped bike
# print(popped_motorcycle) # popped bike was put into its own variable


# you can pop items from any position in a list!

#first_owned = motorcycles.pop(0)
#print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#print(motorcycles)


# motorcycles[0] = 'ducati'
# motorcycles.append('ducati')
# motorcycles.insert(2, 'ducati')
# del motorcycles[1]
