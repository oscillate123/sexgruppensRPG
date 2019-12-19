from artificialintelligence import AI_class
from map import map
from room import room
from Fight import Fight
from Hero import Hero, Knight, Rouge, Wizard
from Monsters import GiantSpider,Orc,Skeleton,Troll,Orc
import random
import inspect

class ai_main:
	def __init__(self,):

		self.map = map(grid_size=4)
		self.hero = Knight(hero_name="SKYNET")
		self.ai = AI_class(hero_instance=self.hero, map_instance=self.map)
		self.fight = Fight(hero=self.hero)

	def print_methods(self, attribute):
		x = inspect.getmembers(attribute, predicate=inspect.ismethod)
		print()
		print()
		print(attribute.__class__.__name__)
		for i in x:
			for y in i:
				if type(y) is str:
					print(y)

	def print_all(self):
		self.print_methods(self.map)
		self.print_methods(self.hero)
		self.print_methods(self.ai)
		self.print_methods(self.fight)

	def text_file(self):
		with open("struktur.txt", "w+") as open_file:
			open_file.write(self.print_all())

if __name__ == "__main__":
	input("Vilken hero")
	main = ai_main()
	main.print_all()
	main.text_file()

	