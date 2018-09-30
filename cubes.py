# make a list of the first 10 cubes 
# (that is, the cube of each integer from 1 through 10)

cubes = [value**3 for value in range (1,11)]



# use a for loop to print out the value of each cube

for cube in cubes:
	print(cube)