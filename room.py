class room:
	def __init__(self):
		self.status = "O"
		self.is_in_this_room = True or False
		self.coordinate = [0, 0]

	def ishere(self):
		self.status = "X"



if __name__ == "__main__":
	x = room()
	y = room()
	z = room()
	z.ishere()
	
	lista = [x, y, z]

	for dinmamma in lista:
		print(dinmamma.status)

	for j in lista:
		print(j.status)