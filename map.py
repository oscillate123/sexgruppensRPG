<<<<<<< HEAD
class map:

	# list of methods in this class
	# method : check_cuboid 	--> check what kind of map object the cuboid is (options are available)
	# method : get_nerby_cuboids--> check what kind of map objects nerby cuboids are
	# method : print_map		--> print the map_grid in console
	# method : map_grid 		--> return the attribute map_grid (its a two-dimensional array)
	# method : update_current_cuboid --> updates the current cuboid coordinate (options are available)
	# method : save_cuboid_coordinate --> saves cuboid coordinates, so we can keep track of changes
	# method : cuboid_character_handler --> puts a character on given coordinate (options are available)

	def __init__(self, name=None, grid_size=None):
		self.name = name or "map-instance"
		# provide the map a name (like de_dust2 ;D). Default value is "map-instance"

		self.room_character = "O"
		self.edge_character = " "
		self.mark_character = "X"
		self.room_finished_character = "Ø"
		self.room_unfinished_character = "o"
		self.currentlocation_character = self.mark_character
		self.map_characters_index = self.map_characters_dictionary()
		# class attributes which define how the printed map will look like. This is customizable
=======
import room
>>>>>>> master

class map:

	def __init__(self, grid_size=4):
		self.test = 0
		self.grid_size = grid_size
		self.grid = self.grid_generator()

	def print_map(self):
		# prints the visual grid, we use the second for loop so we do not get the "[]" and the "'"s

		print() 
		visual_grid = []

		for y in self.grid:
			rows = []
			for instance in y:
				rows.append(instance.status)
			visual_grid.append(rows)
				
		for row in visual_grid:
			print(" ".join(row))

	def grid_generator(self):
		# one grid with all the room-instances
		# its a two dimensional array, "outer array" is y-axis and the y-axis elements
		# are the x-"axises" and the x-axis elements

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
<<<<<<< HEAD
					width.append(self.edge_character)
			length.append(width)

		return length

	def map_characters_dictionary(self):
		map_index_dictionary = {
			"room_character": self.room_character,
			"edge_character": self.edge_character,
			"mark_character": self.mark_character,
			"room_finished_character": self.room_finished_character,
			"room_unfinished_character": self.room_unfinished_character,
			"currentlocation_character": f"Same as mark_character: '{self.mark_character}'"
		}

		return map_index_dictionary

	@staticmethod
	# used for supporting the map class
	def number_pos_or_neg(number):
		if number > -1:
			return number
		else:
			return False

	def map_object_character_checker(self, string, error_msg=f"Unknown character: "):

		# TODO: new idea, make index with the characters that mean something. Loop the elements
		# TODO: letters through the "index" and return values depending on the amount of matches

		try:
			if string == self.room_character:
				return "room"
			elif string == self.edge_character:
				return "edge"
			elif string == self.currentlocation_character:
				return "current-location"
			else:
				return error_msg + string
		except Exception as e:
			print(f'General error. Check map.map_object_character_checker, the input was "{string}"')

	def map_grid(self):
		return self.map_grid

	def print_map(self):
		print() # make a new row
		self.map_adjustments()
		for y in self.map_grid:
			print(" ".join(y))
		print() # make a new row

	def check_cuboid(self, coordinate, option):
=======
					z = x + y
					z = room.room(coordinate=[y, x], status=room.room().edge_character, edge=True)
					row_rooms.append(z)

			rooms_grid.append(row_rooms)

		return rooms_grid	

	def update_room(self, coordinate, update=""):
		# updates the status of a room
		if update == "unfinished":
			self.grid[coordinate[0]][coordinate[1]].unfinished()
		elif update == "finished":
			self.grid[coordinate[0]][coordinate[1]].finished()
		elif update == "is_here":
			self.grid[coordinate[0]][coordinate[1]].is_here()
		elif update == "edge":
			self.grid[coordinate[0]][coordinate[1]].edge()

	def where_am_i(self, option="return"):
		# returns the position of the room the person is in
		for y_axis in self.grid:
			for x_axis in y_axis:
				if x_axis.status == room.room().mark_character:
					if option == "return":
						return x_axis.coordinate
					elif option == "print":
						print(x_axis.coordinate)

	def get_room(self, coordinate):
		# coordinate needs to be a list, e.g. [1, 2]
		# this method returns a room-instance element from the grid arrays
>>>>>>> master
		y, x = coordinate

		return self.grid[y][x]

	def nerby_rooms(self):
		# provides a dictionary with the data of above, below, right and left rooms

		y_axis, x_axis = self.where_am_i()

		nearby_cubiods_data = {
			'above': {
				'coordinate': self.get_room(coordinate=[y_axis-1, x_axis]).coordinate,
				'status': self.get_room(coordinate=[y_axis-1, x_axis]).status
				},
			'below': {
				'coordinate': self.get_room(coordinate=[y_axis+1, x_axis]).coordinate,
				'status': self.get_room(coordinate=[y_axis+1, x_axis]).status
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

