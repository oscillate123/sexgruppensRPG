from os import system, name
import sys, time
from map import map as map
from Monsters import *
from Hero import *
import json
from pathlib import Path


folder = Path("json_file")
folder.mkdir(exist_ok=True)

with open("json_file\saved_heroes.json", "r") as open_file:
	dict_list = json.load(open_file)
	saved_character_list = []
	for value in dict_list:
		if dict_list[value]["Type"] == "Knight":
			knight = Knight(value)
			knight.score = dict_list[value]["Score"]
			saved_character_list.append(knight)
		elif dict_list[value]["Type"] == "Rouge":
			rouge = Rouge(value)
			rouge.score = dict_list[value]["Score"]
			saved_character_list.append(rouge)
		elif dict_list[value]["Type"] == "Wizard":
			wizard = Wizard(value)
			wizard.score = dict_list[value]["Score"]
			saved_character_list.append(wizard)

def clear_screen():
	if name == 'nt':
		_ = system('cls')
	
def print_slow(str):
	str = str + "\n"
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.02)

def load_hero():
	if len(saved_character_list) != 0:
		print("Saved heroes: \n")
		for item in saved_character_list:
			print(item)
		print("Write the name of the hero you want to play with!")
		name_select = input("\n --> ")
		for item in saved_character_list:
			item = str(item)
			if name_select in item:
					dict_keys= (dict_list.keys())
					for name in dict_keys:
						name = str(name)
						if name == name_select:
							if dict_list[name]["Type"] == "Knight":
								knight = Knight(name)
								knight.score = dict_list[name]["Score"]

							elif dict_list[name]["Type"] == "Wizard":
								wizard = Wizard(name)
								wizard.score = dict_list[name]["Score"]

							elif dict_list[name]["Type"] == "Rouge":
								rouge = Rouge(name)
								rouge.score = dict_list[name]["Score"]

		print(f"The hero '{name_select}' has been selected!")
		print_slow("-"*20)
		input("Press enter to continue")
	else:
		print("No heroes saved!")
		start_menu()

def save_character_to_json():
	with open("json_file\saved_heroes.json", "w+") as close_file:
		close_file.seek(0)
		close_file.truncate()
		json.dump(dict_list, close_file)
		close_file.close()

def update_score(hero_name, score, object):
	dict_list[hero_name]["Score"] = score
	saved_character_list[saved_character_list.index(object)] = object
	save_character_to_json()

def save_character():
	if len(created_character_list) != 0:
		print("Created heroes: ")
		for item in created_character_list:
			print(item)
		print("Type in the name of the hero you want to save!")
		name_select = input("\n --> ")

		for item in created_character_list:
			item = str(item)
			if name_select in item:
				if item in saved_character_list:
					saved_character_list.replace(item)
			save_character_to_json()
			print("Hero saved!\n")
			start_menu()
	else:
		print("A hero needs to be created in order to be saved!\n")

def ask_to_save():
	print_slow(" do you want to save your character at this point?")
	print_slow("@ 1 Save")
	print_slow("@ 2 Continue exploring")
	try:
		answer = int(input('\n --> '))
	except ValueError:
		print_slow("Wrong input")
	if (answer == 1):
		save_character()
	else:
		return

def grid_menu():
	clear_screen()
	print_slow("-"*20)
	print_slow("A true hero needs a map to explore, please choose a grid size suitable for your adventure")
	print_slow("The available options are as follows :")
	print_slow("@ 4 for 4x4 grid")
	print_slow("@ 5 for 5x5 grid")
	print_slow("@ 8 for 8x8 grid")
	print_slow("-"*20)
	grid_select = int(input('\n --> '))
	if grid_select != 4 and grid_select != 5 and grid_select != 8:
		print_slow("Wrong input please follow the instructions correctly")
	else:
		return grid_select

def hero_menu():
	clear_screen()
	hero_selected = False
	hero_name = str
	print_slow("-" * 20)
	print_slow("Welcome to Dungeon run now it's time to choose your hero: ")
	print_slow("The available options are as follows :")
	print_slow("@ 1 for Knight")
	print_slow("@ 2 for Rogue")
	print_slow("@ 3 for Wizard")
	print_slow("-" * 20)
	try:
		hero_select = int(input('\n --> '))
	except ValueError:
		print_slow("Wrong input")

	if (hero_select == 1):
		print_slow("You have choosen the Knight! ")
		print_slow("Give your hero a name! ")
		hero_name_try = input("\n --> ")
		hero_name = validate(hero_name_try)
		hero_selected = True
		knight = Knight(hero_name)
		knight.print_stats()
		knight.add_hero_dict(dict_list)
		saved_character_list.append(knight)
		save_character_to_json()
		knight.score= 5
		update_score(knight.hero_name, knight.score, knight)
		print_slow("-" * 20)
		input("Press enter to continue")

	elif (hero_select == 2):
		print_slow("You have choosen the Rogue! ")
		print_slow("Give your hero a name! ")
		hero_name_try = input("\n --> ")
		hero_name = validate(hero_name_try)
		hero_selected = True
		rouge = Rouge(hero_name)
		rouge.print_stats()
		rouge.add_hero_dict(dict_list)
		saved_character_list.append(rouge)
		save_character_to_json()
		rouge.score = 10
		update_score(rouge.hero_name, rouge.score, rouge)
		print_slow("-" * 20)
		input("Press enter to continue")
	
	elif (hero_select == 3):
		print_slow("You have choosen the Wizard! ")
		print_slow("Give your hero a name! ")
		hero_name_try = input("\n --> ")
		hero_name = validate(hero_name_try)
		hero_selected = True
		wizard = Wizard(hero_name)
		wizard.print_stats()
		wizard.add_hero_dict(dict_list)
		saved_character_list.append(wizard)
		save_character_to_json()
		wizard.score = 10
		update_score(wizard.hero_name, wizard.score, wizard)
		print_slow("-" * 20)
		input("Press enter to continue")

	else:
		print_slow("Wrong input! Please read the instructions")
	if hero_selected is True:
		return hero_name


def validate(hero_name):
	dict_key = dict_list.keys()
	for name in dict_key:
		name = str(name)
		if name == hero_name:
			while True:
				print_slow("Name already in use!")
				print_slow("Choose a new name")
				hero_name = input("\n --> ")
				if hero_name != name:
					break
	return hero_name


def spawn_menu():
	clear_screen()
	spawn_selected = False
	spawn_select = 0
	spawn_coordinates = []

	print_slow("-" * 20)
	print_slow("Pick a spawn point on the map: ")
	print_slow("@ 1 for NorthWest")
	print_slow("@ 2 for NorthEast")
	print_slow("@ 3 for SouthWest")
	print_slow("@ 4 for SouthEast")
	print_slow("-" * 20)

	try:
		spawn_select = int(input('\n --> '))
	except ValueError:
		print_slow("Wrong input")

	if spawn_select == 1:
		spawn_point = "NW"
		spawn_selected = True
		spawn_coordinates = [0, 0]
	elif spawn_select == 2:
		spawn_point = "NE"
		spawn_selected = True
		spawn_coordinates = [0, 5]
	elif spawn_select == 3:
		spawn_point = "SW"
		spawn_selected = True
		spawn_coordinates = [5, 0]
	elif spawn_select == 4:
		spawn_point = "SE"
		spawn_selected = True
		spawn_coordinates = [5, 5]

	if spawn_selected:
		current_run = map(name="demo_run")
		#current_run.update_current_cuboid(coordinate=spawn_coordinates)
		map_object = current_run.check_cuboid(coordinate=current_run.current_cuboid, option='return')
		print_slow(f"Your spawnpoint is on the {map_object}, at coordinate {current_run.current_cuboid}")
		current_run.print_map()  

def start_menu():
	while True:
		grid_size = 0
		clear_screen()
		print_slow(" \n Dungeon Run \n")
		print_slow("-"*20)
		print_slow("@ 1 New Game")
		print_slow("@ 2 Load Game")
		print_slow("@ 3 Quit")
		print_slow("-"*20)
		try:
			sub_meny = int(input('\n --> '))
		except ValueError:
			print_slow("Wrong input")
			continue

		if (sub_meny == 1):
			hero_name = hero_menu()
			grid_select = grid_menu()
			spawn_point = spawn_menu()
		elif (sub_meny == 2):
			load_hero()
			grid_select = grid_menu()
			spawn_point = spawn_menu()

		elif (sub_meny == 3):
			print_slow("BYEEEEEEEE")
			exit()

start_menu()
