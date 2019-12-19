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
		self.map_size = 4
		self.map = map(grid_size=self.map_size)
		self.hero = Knight(hero_name="SKYNET")
		self.ai = AI_class(hero_instance=self.hero, map_instance=self.map)
		self.fight = Fight(hero=self.hero)

	def main_loop(self):
		pass


	def text_file(self, attribute):
		x = inspect.getmembers(attribute, predicate=inspect.ismethod)
		strings = "\n\n"
		strings = strings + attribute.__class__.__name__
		for i in x:
			for y in i:
				if type(y) is str:
					strings = strings + "\n" + y
		return strings
	def to_text_file(self, string):
		with open("struktur.txt", "w+") as open_file:
			open_file.write(string)
	def text_all(self):
		super_txt = self.text_file(self.map) + self.text_file(self.hero) + self.text_file(self.ai) + self.text_file(self.fight)
		self.to_text_file(string=super_txt)

if __name__ == "__main__":
	main = ai_main()
	main.main_loop()

	