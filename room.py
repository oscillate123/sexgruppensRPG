class room:
	def __init__(self, name="", status="", coordinate=[], edge=False):
		self.name = name

		self.room_character = "O"
		self.edge_character = "-"
		self.mark_character = "X"
		self.room_finished_character = "Ø"
		self.room_unfinished_character = "o"

		self.status = status
		self.coordinate = coordinate
		self.edge = edge

	def is_here(self):
		self.status = self.mark_character

	def unfinished(self):
		self.status = self.room_unfinished_character

	def finished(self):
		self.status = self.room_finished_character

	def fight(self):
		return

	def get_coordinate(self):
		return self.coordinate

	def if_edge(self):
		# method for checking if the room is an edge or a room
		if self.status == self.edge_character:
			return True
		else:
			return False



if __name__ == "__main__":

	def grid_generator(grid_size_with_edge=6):
		# generates two grids, one grid with all the symbols of the

		number = grid_size_with_edge
		rooms_grid = []

		for y in range(number):
			row_rooms = []
			for x in range(number):
				if x is not 0 and x is not max(range(number)):
					if y is not 0 and y is not max(range(number)):
						z = x + y
						z = room(coordinate=[y, x], status=room().room_character, edge=False)
						row_rooms.append(z)
					else:
						z = x + y
						z = room(coordinate=[y, x], status=room().edge_character, edge=True)
						row_rooms.append(z)
				else:
					z = x + y
					z = room(coordinate=[y, x], status=room().edge_character, edge=True)
					row_rooms.append(z)

			rooms_grid.append(row_rooms)

		return rooms_grid

	def print_map(arrays):
		print() # make a new row
		for y in arrays:
			for x in y:
				print(x.status)
				# test to print the letters on one row
		print() # make a new row


	x = grid_generator()
	print_map(x)








