from dice import*
from Fight2 import Fight as prev_fight
from Hero import Hero, Knight, Rouge, Wizard
from Monsters import*
from os import system
from numpy.random import choice
import random

class fight:
    def __init__(self, hero):
    	self.hero = hero
    	self.monsters = self.old_gen_monsters()
    	self.start = None



    def try_to_run(self):
        temp = self.hero.agility * 10
        escape_procent = temp / 100

        if self.hero.__class__.__name__ == "Wizard":
            escape_procent = self.hero.special_skill()

        rest_procent = 1 - escape_procent
        value_points = [True, False]
        probabilities = [escape_procent, rest_procent]
        escape_or_not = choice(value_points, p=probabilities)

        return escape_or_not

    def old_gen_monsters(self):
    	x = prev_fight(hero="hero")
    	return prev_fight(hero="hero").generate_monster()

    def print_types(self):
    	# prints all the types
    	types_dict = {}
    	types_dict["self.hero"] = self.hero
    	types_dict["self.monsters"] = self.monsters
    	types_dict["self.try_to_run"] = self.try_to_run()

    	for i in types_dict:
    		print()
    		print("#", i)
    		print("##", types_dict[i])

    		if i == "self.monsters":
    			print("##", len(types_dict["self.monsters"]))

    def who_starts(self):
        for character in self.character_fight_list:
            character.start_score = n_dice(character.initiative)

        self.character_fight_list.sort(key=lambda x: x.start_score, reverse=True)

    def if_draw(self):
    	self.start = self.hero





if __name__ == "__main__":

	system('clear')

	hero_msg_input = """
1 - Knight
2 - Rouge
3 - Wizard
	"""
	print(hero_msg_input)
	# hero_int = int(input(f"{hero_msg_input}"))
	hero = Knight("Testing")
	hero_int = 1

	if hero_int == 1:
		hero = Knight("Knight Test")
	elif hero_int == 2:
		hero = Rouge("Rouge Test")
	elif hero_int == 3:
		hero = Wizard("Wizard Test")

	x = fight(hero=hero)

	x.print_types()