# from random import randrange

class map:

	def __init__(self, name):
		self.name = name

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

	def check_cuboid(self, coordinate, mode):
		y, x = coordinate

		y = self.number_pos_or_neg(y)
		x = self.number_pos_or_neg(x)

		mode = mode
		shrug = r'¯\_(ツ)_/¯'
		error = f"error! in map.check_cuboid. Name: {self.name} {shrug}"

		if y is not False and x is not False:

			if mode == "test":
				if self.map_grid[y][x] == '#':
					print("Room")
				elif self.map_grid[y][x] == '_':
					print("Edge")
				else:
					print(error)
			elif mode == "options":
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
			if mode == "test":
				print('Out of map')
			elif mode == "options":
				return 'Out of map'
			else:
				print(error)
				return error

	def get_nerby_cuboids(self):
		nearby_cubiods_data = {
			'above': {
				'coordinate': self.cuboid_above,
				'map object type': self.check_cuboid(self.cuboid_above, 'options')
				},
			'below': {
				'coordinate': self.cuboid_below,
				'map object type': self.check_cuboid(self.cuboid_below, 'options')
				},
			'right': {
				'coordinate': self.cuboid_right,
				'map object type': self.check_cuboid(self.cuboid_right, 'options')
				},
			'left': {
				'coordinate': self.cuboid_left,
				'map object type': self.check_cuboid(self.cuboid_left, 'options')
				}
			}
		return nearby_cubiods_data

	def update_current_cuboid(self, coordinate):
		# used for updating the self.current_cuboid coordinate
		pass


if __name__ == "__main__":
	game = map('testing')
	print(f"\n{game.name}\n")
	game.print_map()
	game.check_cuboid(game.current_cuboid, 'test')

	nerby_cubids_data = game.get_nerby_cuboids()
	
	for element in nerby_cubids_data:
		print()
		print(element)
		print(nerby_cubids_data[element])
		print()

