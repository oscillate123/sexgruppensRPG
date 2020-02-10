from artificialintelligence import AI_class
from map import map
from room import room
from Fight import Fight
from Hero import Hero, Knight, Rouge, Wizard
from Monsters import GiantSpider,Orc,Skeleton,Troll,Orc
import random
import inspect
import time
from other_functions import clear_screen

class ai_main:
	def __init__(self, grid_size, hero_instance):
		self.map_size = grid_size
		self.map = map(grid_size=self.map_size)
		self.hero = hero_instance
		self.ai = AI_class(hero_instance=self.hero, map_instance=self.map)
		self.fight = Fight(hero=self.hero, is_Ai=True)
		self.room = room()
		self.round_count = 0
		self.game_active = True
		self.round_max = 5
		self.stop_value = self.map_size**2

	def main_loop(self):

		while self.game_active:
			if self.round_count == 0: # sets a random spawn point
				spawn = self.ai.spawn_select(grid_select=self.map_size)
				spawn = self.map.get_room(coordinate=spawn)
				spawn.is_here()
				self.round_count += 1
				clear_screen() #clear
				self.pmap() #print
				time.sleep(2) #wait
			else: 
				# updates old room and sets new room to X
				current_coordinate = self.where_am_i() # hämta kordinater
				new_coordinate = self.new_move_coordinate() # ny random kordinat runtomkring
				self.update_old_room(coordinate=current_coordinate)
				self.ai.ai_rooms_add(current_coordinate) # statics
				self.mark_new_room(coordinate=new_coordinate)
				self.round_count += 1 #add round count
				room = self.get_room(new_coordinate)
				clear_screen() #clear
				self.pmap() #print map
				time.sleep(2) #wait

				# fight
				room.fight_generator(hero_instance=self.hero, is_ai=True)
				monster_list = room.fight.monsters_list
				room.fight.ai_choice_number = self.ai.ai_choice(self.ai.fight_or_run(monster_list))
				win_or_not = room.fight.run_fight()
				self.ai.ai_monsters_killed(room.fight.update_monster_killed_number)
				self.fight_win_or_not(win_or_not)
				self.ai.ai_treasure_collected(treasure_points=room.total_loot)
				room.total_loot = 0

				if self.hero.health == 0:
					self.ai.ai_won_game_or_done()
					self.game_active = False

			if self.round_count > self.round_max: # max limit, atm för loopen
				self.game_active = False # för att få stop på loopen
				self.ai.ai_won_game_or_done()

			if self.round_count == self.stop_value:
				self.game_active = False # för att få stop på loopen
				self.ai.ai_won_game_or_done()

	def update_old_room(self, coordinate): # uppdaterar gamla rummet till klart
		self.map.update_room(coordinate=coordinate, update="finished")

	def fight_win_or_not(self, response):
		if response == "win":
			self.ai.ai_won_fight()

	def where_am_i(self): # var är jag nu
		return self.map.where_am_i(option="return")

	def new_move_coordinate(self): # gå till ny coordinate (returnerar coordinate)
		return self.ai.new_move()

	def get_room(self, coordinate): # hämta ett rum (instans)
		return self.map.get_room(coordinate=coordinate)

	def mark_new_room(self, coordinate): # markera rummet med ett X
		new_room = self.get_room(coordinate)
		new_room.is_here()

	def pmap(self): # printa mapp
		self.map.print_map()

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
		super_txt = self.text_file(self.map) + self.text_file(self.hero) + self.text_file(self.ai) + self.text_file(self.fight) + self.text_file(self.room)
		self.to_text_file(string=super_txt)


	