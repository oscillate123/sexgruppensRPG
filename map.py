from random import randrange


class map:

	def __init__(self):
		# self.user_grid_req = randrange(4, 9)
		self.user_grid_req = 5
		self.map_grid_number = self.user_grid_req + 2
		self.map_grid = map.grid(self.map_grid_number)

	@staticmethod
	def grid(number):
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

	def map_grid(self):
		return self.map_grid

	def print_map(self):
		for y in self.map_grid:
			print(y)
		return

	def check_coordinate(self):
		pass


x = map()

x.print_map()