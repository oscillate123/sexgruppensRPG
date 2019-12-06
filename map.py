# from random import randrange

class map:

	# list of methods in this class
	# method : check_cuboid 	--> check what kind of map object the cuboid is (options are available)
	# method : get_nerby_cuboids--> check what kind of map objects nerby cuboids are
	# method : print_map		--> print the map_grid in console
	# method : map_grid 		--> return the attribute map_grid (its a two-dimensional array)
	# method : update_current_cuboid --> updates the current cuboid coordinate (options are available)

	def __init__(self, name):
		self.name = name
		# provide the map a name (like de_dust2 ;D)

		self.user_grid_req = 5
		# self.user_grid_req = randrange(4, 9)
		# replace self.user_grid_req = 5 with above line if you want random map size
		# you also need to uncomment "from random import randrange" on line 1

		self.map_grid_number = self.user_grid_req + 2 
		# +2 because we want to make edges
		# use self.print_map() if you want a visual, '_' is an edge, '#' is a room.

		self.map_grid = self.grid_generator(self.map_grid_number) 
		# self.map_grid is a two dimensional array which is the map

		self.current_cuboid = [0, 0]  
		# [Y, X] --> y is y-axis and x is x-axis, like a coordinate system
		
		self.cuboid_above = [self.current_cuboid[0] - 1, self.current_cuboid[1]]
		self.cuboid_below = [self.current_cuboid[0] + 1, self.current_cuboid[1]]
		self.cuboid_right = [self.current_cuboid[0], self.current_cuboid[1] + 1]
		self.cuboid_left = [self.current_cuboid[0], self.current_cuboid[1] - 1]
		# class attributes that indicates what nerby cuboids are on the grid

	@staticmethod
	# used for supporting the map class
	def grid_generator(number):
		length = []

		for y in range(number):
			width = []
			for x in range(number):
				if x is not 0 and x is not max(range(number)):
					if y is not 0 and y is not max(range(number)):
						width.append('#')
					else:
						width.append('_')
				else:
					width.append('_')
			length.append(width)

		return length

	@staticmethod
	# used for supporting the map class
	def number_pos_or_neg(number):
		if number > -1:
			return number
		else:
			return False

	def map_grid(self):
		return self.map_grid

	def print_map(self):
		for y in self.map_grid:
			print(y)
		return

	def check_cuboid(self, coordinate, option):
		y, x = coordinate

		y = self.number_pos_or_neg(y)
		x = self.number_pos_or_neg(x)

		shrug = r'¯\_(ツ)_/¯'
		error = f"error! in map.check_cuboid. Name: {self.name} {shrug}"

		if y is not False and x is not False:

			if option == "test":
				if self.map_grid[y][x] == '#':
					print("Room")
				elif self.map_grid[y][x] == '_':
					print("Edge")
				else:
					print(error)
			elif option == "return":
				if self.map_grid[y][x] == '#':
					return "room"
				elif self.map_grid[y][x] == '_':
					return "edge"
				else:
					return error
			else:
				print(error)
				return error

		else:
			if option == "test":
				print('Out of map')
			elif option == "return":
				return 'Out of map'
			else:
				print(error)
				return error

	def get_nerby_cuboids(self):
		# provides a dictionary with the data of above, below, right and left cuboids
		nearby_cubiods_data = {
			'above': {
				'coordinate': self.cuboid_above,
				'map_object_type': self.check_cuboid(self.cuboid_above, option='return')
				},
			'below': {
				'coordinate': self.cuboid_below,
				'map_object_type': self.check_cuboid(self.cuboid_below, option='return')
				},
			'right': {
				'coordinate': self.cuboid_right,
				'map_object_type': self.check_cuboid(self.cuboid_right, option='return')
				},
			'left': {
				'coordinate': self.cuboid_left,
				'map_object_type': self.check_cuboid(self.cuboid_left, option='return')
				}
			}
		return nearby_cubiods_data

	def update_current_cuboid(self, coordinate, option='empty'):
		# used for updating the self.current_cuboid coordinate
		# mode='empty' is a default value, so we are not forced to provide option everytime we invoke the method
		self.current_cuboid = coordinate

		if option == "return":
			return self.current_cuboid
		else:
			pass


if __name__ == "__main__":
	import time

	# this code will only run if you run the file directly.
	# If you refer/invoke the class, below code will not run.

	game = map('default_map_5x5')
	print(f"below we test class attributes, methods and static methods. we print the results for manual correction")
	print(f"\n{game.name}\n")

	game.print_map()
	game.check_cuboid(game.current_cuboid, option='test')
	nerby_cubids_data = game.get_nerby_cuboids()
	
	print()

	for element in nerby_cubids_data:
		time.sleep(1)
		print(element)
		print(nerby_cubids_data[element])
		print()

	game.update_current_cuboid(coordinate=[1, 1])
	print(game.current_cuboid)
	game.check_cuboid(game.current_cuboid, option='test')

	print('updating current_cuboid from [1, 1] --> [4, 3]')

	game.update_current_cuboid(coordinate=[4, 3])
	print(game.current_cuboid)
	game.check_cuboid(game.current_cuboid, option='test')

