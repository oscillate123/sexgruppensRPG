try:
	import requests
	import webbrowser
	import random
	import json
	from Hero import *
	from Fight import *
	from room import *
	from pathlib import Path
	from spotify import spotify
except Exception as e:
	print(e, "run -> 'pip install requests' for dope features")

class AI:

	def __init__(self, hero_instance, map_instance):
		self.hero = hero_instance
		self.map = map_instance
		self.name = "Skynet"
		self.theme_lyrics = f"{self.name}: Dundun dededun Dundun dededun doodoodoo dooo do doo doodoodoo dooo DO deDOO"

		self.fights_won = 0
		self.rooms_visited_coordinates = []
		self.rooms_visited_amount = len(self.rooms_visited_coordinates)
		self.monsters_killed = 0
		self.treasure_collected = 0

	def api_theme_song_open_in_browser(self):
		auth = spotify().auth
		headers = spotify().head
		uri_id = "3dAUz8qeUL6pKf6gp6iemq"
		url = f"https://api.spotify.com/v1/tracks/{uri_id}?market=SE"
		response = requests.get(url=url, headers=headers) # api response
		response_json = response.json() # make it json
		theme_song = response_json.get("preview_url") # get the url of the song
		webbrowser.open_new_tab(url=theme_song) # opens a tab and plays the song

	def ai_won_fight(self):
		self.fights_won += 1

	def ai_monsters_killed(self):
		self.monsters_killed += 1

	def ai_rooms_visited(self, coordinate):
		if coordinate not in self.rooms_visited:
			self.rooms_visited_coordinates.append(coordinate)

	def ai_treasure_collected(self, treasure_points):
		self.treasure_collected += treasure_points

	def return_game_stats(self):
		game_stats = {
			"fights_won": self.fights_won,
			"rooms_won": self.fights_won,
			"rooms_visited": self.rooms_visited_amount,
			"monsters_killed": self.monsters_killed,
			"treasure_points": self.treasure_collected	
		}
		return game_stats

	def json_sorter(self, data):
		return json.dumps(data, indent=4, sort_keys=True)

	def random_map_move(self):
		options = self.map_instance.nerby_rooms()

		print(json_sorter(options)) # should return different options in a dictionary
		# TODO: LOOP through and choose one of the options based on default_health

	def ai_choice(self, math_result):

		if math_result == "run":
			ai_choice = 2
		elif math_result == "fight":
			ai_choice = 1
		elif math_result == "dumb_retard_ai":
			value_points = ['1', '2']
			probabilities = [0.7, 0.3]
			ai_choice = random_value = (choice(value_points, p=probabilities))

		return ai_choice

	def fight_or_run(self, monster_list):

		total_attack = []
		total_agility = []
		total_health = []
		monster_names = []

		for monster in monster_list:
			total_attack.append(monster.attack)
			total_agility.append(monster.agility)
			total_health.append(monster.health)
			monster_names.append(monster.__class__.__name__)

		if total_attack/self.hero.health > 2 and self.hero.__class__.__name__ == "Wizard":
			if len(monster_list) > 2
				if "Troll" in monster_names:
					return "run"
				else:
					return "fight"
			else:
				return "fight"
			return "run"

		elif total_attack/self.hero.health > 2.5 and self.hero.__class__.__name__ == "Knight":
			if len(monster_list) > 2
				if "Troll" in monster_names:
					return "run"
				else:
					return "fight"
			else:
				return "fight"

		elif total_attack/self.hero.health > 2.5 and self.hero.__class__.__name__ == "Rouge":
			if len(monster_list) > 3
				if "Troll" in monster_names:
					return "run"
				else:
					return "fight"
			else:
				return "fight"

		else:
			return "fight"



if __name__ == "__main__":

	ex_hero = Knight(name="dinmamma")
	ex_map = map()
	ex_map.update_room(coordinate=[1, 1], update="is_here")
	
	x = AI(hero=ex_hero)

	print(x.ai_choice(math_result="dumb_retard_ai"))
	print(x.random_map_move())

	x.api_theme_song_open_in_browser()