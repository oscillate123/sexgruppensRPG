
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
		self.edge_character = "_"
		self.mark_character = "X"
		self.currentlocation_character = self.mark_character
		# class attributes which define how the printed map will look like. This is customizable

		self.user_grid_req = grid_size or 5
		# default value is 5, unless custom number is given

		self.map_grid_number = self.user_grid_req + 2 
		# +2 because we want to make edges
		# use self.print_map() if you want a visual, '_' is an edge, '#' is a room.

		self.map_grid = self.grid_generator()
		# self.map_grid is a two dimensional array which is the map

		self.current_cuboid = [0, 0]
		# [Y, X] --> y is y-axis and x is x-axis, like a coordinate system
		# keeps track of where you are on the map

		self.previous_cuboids = []
		# saves the previous coordinate values of self.current_cuboid
		
		self.cuboid_above = [self.current_cuboid[0] - 1, self.current_cuboid[1]]
		self.cuboid_below = [self.current_cuboid[0] + 1, self.current_cuboid[1]]
		self.cuboid_right = [self.current_cuboid[0], self.current_cuboid[1] + 1]
		self.cuboid_left = [self.current_cuboid[0], self.current_cuboid[1] - 1]
		# class attributes that indicates what nerby cuboids are on the grid

	# used for supporting the map class
	def grid_generator(self):
		number = self.map_grid_number
		length = []

		for y in range(number):
			width = []
			for x in range(number):
				if x is not 0 and x is not max(range(number)):
					if y is not 0 and y is not max(range(number)):
						width.append(self.room_character)
					else:
						width.append(self.edge_character)
				else:
					width.append(self.edge_character)
			length.append(width)

		return length

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
			print(y)
		print() # make a new row

	def check_cuboid(self, coordinate, option):
		y, x = coordinate

		y = self.number_pos_or_neg(y)
		x = self.number_pos_or_neg(x)

		shrug = r'¯\_(ツ)_/¯'
		error = f'error! {shrug} Look in map.check_cuboid.\nInstance name: "{self.name}"\nCoordinate: {coordinate}\nOption: {option}'

		if y is not False and x is not False:
			ccc = self.map_grid[y][x]
			# ccc is a shortening for cuboid coordinate character

			ccc_discription = self.map_object_character_checker(ccc)

			if option == "print":
				print(f'{coordinate} is ', ccc_discription)
			elif option == "return":
				return ccc_discription

		else:
			if option == "print":
				print('out of map')
			elif option == "return":
				return 'out of map'
			else:
				print(error)
				return error

	def get_nerby_cuboids(self):
		# provides a dictionary with the data of above, below, right and left cuboids
		# TODO: CHECK self.check_cuboid() "todo's" xD
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

	def save_cuboid_coordinate(self, coordinate):
		# saves cuboid coordinates, so the instance of this class can keep track on coordinate history
		self.previous_cuboids.append(coordinate)

	def update_current_cuboid(self, coordinate, option=''):
		# used for updating the self.current_cuboid coordinate
		# mode='empty' is a default value, so we are not forced to provide option everytime we invoke the method

		not_updated_coordinate = self.current_cuboid # before we update
		self.save_cuboid_coordinate(self.current_cuboid)

		if option == "return":
			self.current_cuboid = coordinate
			return self.current_cuboid

		elif option == "print":
			self.current_cuboid = coordinate
			print('Current coordinate: ', self.current_cuboid)

		elif option == "move":
			# TODO: this doesn't make the "previous" 'X' smaller for some reason
			self.cuboid_character_handler(
					option="replace", 
					new_character="x",
					replace_character="X",
					coordinate=not_updated_coordinate
				)

			self.current_cuboid = coordinate # now we update the coordinate
			self.cuboid_character_handler(new_character="X", option="mark", coordinate=coordinate)


	def cuboid_character_handler(self, new_character="", option="", replace_character="", coordinate=[]):
		# the method puts a character on the the give coordinate
		# if no coordinate, self.current_cuboid will be used
		# OPTIONS are available, options list --> [mark, replace, room_finished, room_unfinished]

		inputs = {
			"new_character": new_character,
			"option": option,
			"replace_character": replace_character,
			"coordinate": coordinate
		}
		
		if not coordinate:
			coordinate = self.current_cuboid

		if option == "mark":
			self.map_grid[coordinate[0]][coordinate[1]] += new_character
		elif option == "replace":
			self.map_grid[coordinate[0]][coordinate[1]].replace(replace_character, new_character)
		elif option == "room_finished":
			self.map_grid[coordinate[0]][coordinate[1]].replace(self.room_character, "Ø")
		elif option == "room_unfinished":
			self.map_grid[coordinate[0]][coordinate[1]].replace(self.room_character, "o")	
		else:
			print(f"Error in cuboid_character_handler, inputs:\n{inputs}\n")

		self.map_adjustments()

	def map_adjustments(self):
		# makes all the elements the same length. 
		# len(element) is the same on all elements in the two-dimensional "map"-array

		longest_element = 1 # the default length on every element is 1
		map_arrays = self.map_grid

		# finds out which is the longest element of all elements on the map
		for y_led in map_arrays:
			for x_led in y_led:
				if len(x_led) > longest_element:
					longest_element = len(x_led)

		# makes all the elements as long as the longest element
		for y_idx, y_led in enumerate(map_arrays):
			for x_idx, x_led in enumerate(y_led):
				if len(x_led) < longest_element:
					difference = longest_element - len(x_led)
					supplement = ' ' * difference
					self.map_grid[y_idx][x_idx] += supplement





if __name__ == "__main__":
	# tests

	# this code will only run if you run the file directly.
	# If you refer/invoke the class, below code will not run.

	def req_valid_input():
		# code requests valid input from user using recursion
		user_input = 0
		
		while user_input > 8 or user_input < 4:
			try:
				user_input = int(input("How big do you want it to be? ;) 4x4 up to 8x8. Type only 1 digit."))
			except ValueError as e:
				print(str(e), " Please type a number between 4 and 8.")
				pass

		return user_input


	map_size = req_valid_input()
	game = map(name='testing_map_class', grid_size=map_size)
	print(f"\n\nbelow we test class attributes, methods and static methods. we print the results for manual correction")
	print(f"\n{game.name}\n")

	game.cuboid_character_handler(new_character="X", option="mark", coordinate=game.current_cuboid)
	game.print_map()
	game.check_cuboid(game.current_cuboid, option='print')
	nerby_cubids_data = game.get_nerby_cuboids()
	
	print()

	for element in nerby_cubids_data:
		print(element)
		print(nerby_cubids_data[element])

	game.update_current_cuboid(coordinate=[0, 1], option='move')
	game.print_map()
	# print()
	# print('updating current_cuboid from [0, 1] --> [4, 3]...')
	# print()
	# game.update_current_cuboid(coordinate=[4, 3], option='print')
	# game.check_cuboid(game.current_cuboid, option='print')
	# game.cuboid_character_handler(new_character="X", option="mark", coordinate=game.current_cuboid)
	# game.print_map()
