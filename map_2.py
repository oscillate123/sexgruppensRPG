import room

class map:

	def __init__(self):
		self.test = 0
		self.grid_size = 4
		self.grid = self.grid_generator()

	def print_map(self):
		print() # make a new row

		visual_grid = []

		for y in self.grid:
			rows = []
			for instance in y:
				rows.append(instance.status)
			visual_grid.append(rows)
				
		for row in visual_grid:
			print(" ".join(row))

	def grid_generator(self):
		# generates two grids
		# one grid with all the room-instances
		# one grid with the room-instances.status (a character/symbol)

		number = self.grid_size + 2
		rooms_grid = []

		for y in range(number):
			row_rooms = []
			for x in range(number):
				if x is not 0 and x is not max(range(number)):
					if y is not 0 and y is not max(range(number)):
						z = x + y
						z = room.room(coordinate=[y, x], status=room.room().room_character, edge=False)
						row_rooms.append(z)
					else:
						z = x + y
						z = room.room(coordinate=[y, x], status=room.room().edge_character, edge=True)
						row_rooms.append(z)
				else:
					z = x + y
					z = room.room(coordinate=[y, x], status=room.room().edge_character, edge=True)
					row_rooms.append(z)

			rooms_grid.append(row_rooms)

		return rooms_grid	

	def update_room(self, coordinate, update=""):
		if update == "unfinished":
			self.grid[coordinate[0]][coordinate[1]].unfinished()
		elif update == "finished":
			self.grid[coordinate[0]][coordinate[1]].finished()
		elif update == "is_here":
			self.grid[coordinate[0]][coordinate[1]].is_here()
		elif update == "edge":
			self.grid[coordinate[0]][coordinate[1]].edge()

	def where_am_i(self, option="return"):
		for y_axis in self.grid:
			for x_axis in y_axis:
				if x_axis.status == room.room().mark_character:
					if option == "return":
						return x_axis.coordinate
					elif option == "print":
						print(x_axis.coordinate)

	def get_room(self, coordinate):
		# coordinate needs to be a list, e.g. [1, 2]
		y, x = coordinate

		return self.grid[y][x]

	def nerby_rooms(self):
		# provides a dictionary with the data of above, below, right and left cuboids
		# TODO: Fix new function for looking up all the characters in an element.

		y_axis, x_axis = self.where_am_i()

		nearby_cubiods_data = {
			'above': {
				'coordinate': self.get_room(coordinate=[y_axis+1, x_axis]).coordinate,
				'status': self.get_room(coordinate=[y_axis+1, x_axis]).status
				},
			'below': {
				'coordinate': self.get_room(coordinate=[y_axis-1, x_axis]).coordinate,
				'status': self.get_room(coordinate=[y_axis-1, x_axis]).status
				},
			'right': {
				'coordinate': self.get_room(coordinate=[y_axis, x_axis+1]).coordinate,
				'status': self.get_room(coordinate=[y_axis, x_axis+1]).status
				},
			'left': {
				'coordinate': self.get_room(coordinate=[y_axis, x_axis-1]).coordinate,
				'status': self.get_room(coordinate=[y_axis, x_axis-1]).status
				}
			}
		return nearby_cubiods_data

