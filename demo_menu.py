from os import system, name
import sys, time
from map import map as map
from Monsters import *
from Hero import *
import json
from other_functions import *
from pathlib import Path
from room import  *
from Fight import  *


folder = Path("json_file")
folder.mkdir(exist_ok=True)
try:
	with open("json_file/saved_heroes.json", "r") as open_file:
		dict_list = json.load(open_file)
		saved_character_list = []
		created_character_list = []
		for value in dict_list:
			if dict_list[value]["Type"] == "Knight":
				knight = Knight(value)
				knight.score = dict_list[value]["Score"]
				knight.time_saved = dict_list[value]["Time"]
				saved_character_list.append(knight)
			elif dict_list[value]["Type"] == "Rouge":
				rouge = Rouge(value)
				rouge.score = dict_list[value]["Score"]
				rouge.time_saved = dict_list[value]["Time"]
				saved_character_list.append(rouge)
			elif dict_list[value]["Type"] == "Wizard":
				wizard = Wizard(value)
				wizard.score = dict_list[value]["Score"]
				wizard.time_saved = dict_list[value]["Time"]
				saved_character_list.append(wizard)

except FileNotFoundError:
	with open("json_file/saved_heroes.json", "w+") as open_file:
		open_file.write("{}")
		dict_list = json.load(open_file)
		saved_character_list = []
		created_character_list = []
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

# Here starts all the help functions for the program

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
								created_character_list.append(Knight(name))
								print(created_character_list)
								
								

							elif dict_list[name]["Type"] == "Wizard":
								wizard = Wizard(name)
								wizard.score = dict_list[name]["Score"]

							elif dict_list[name]["Type"] == "Rouge":
								rouge = Rouge(name)
								rouge.score = dict_list[name]["Score"]

		print(f"The hero '{name_select}' has been selected!")
		print_slow("-"*20)
		input("Press enter to continue")
		return True, name_select
	else:
		print("No heroes saved!")
		input("Press enter to continue")
		return	

def save_character_to_json():
	with open("json_file/saved_heroes.json", "w+") as close_file:
		close_file.seek(0)
		close_file.truncate()
		json.dump(dict_list, close_file)
		close_file.close()

def update_score(hero_name, score, object):
	time_now = time.strftime("%m/%d Time %H:%M")
	dict_list[hero_name]["Score"] = score
	dict_list[hero_name]["Time"] = time_now
	saved_character_list[saved_character_list.index(object)] = object
	save_character_to_json()

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
	#return hero_name

# probmlems here!!! "Saved_character_list.replace(item)" är en lista men listor har ingen .replace funktion

def ask_to_save(hero_name):
	print_slow(" Do you want to save your character at this point?")
	print_slow("# 1 Save")
	print_slow("# 2 To Exit Game")
	try:
		answer = int(input('\n --> '))
	except ValueError:
		print_slow("Wrong input")
	if (answer == 1):
		for item in saved_character_list:
			if hero_name == item.hero_name:
				update_score(item.hero_name, 655, item)
			# else:
			# 	print("Couldn't save")
			# 	#input("wait")
	else:
		print_slow("Thanks for playing Dungeon Run!")
		print_slow("Created by: Robert, Sadri, Oliver, Oscar and Emil")
		exit()

def calc_spawnpoint(grid_select,spawn_point):

	spawn_coordinates = []
	if grid_select == 4:
		if (spawn_point == "NE"):
			spawn_coordinates = [1,4]
			return spawn_coordinates
		elif (spawn_point == "SW"):
			spawn_coordinates = [4,1]
			return spawn_coordinates
		elif (spawn_point == "SE"):
			spawn_coordinates = [4,4]
			return spawn_coordinates

	elif (grid_select==5):
		if (spawn_point == "NE"):
			spawn_coordinates = [1,5]
			return spawn_coordinates
		elif (spawn_point == "SW"):
			spawn_coordinates = [5,1]
			return spawn_coordinates
		elif (spawn_point == "SE"):
			spawn_coordinates = [5,5]
			return spawn_coordinates

	elif (grid_select==8):
		if (spawn_point == "NE"):
			spawn_coordinates = [1,8]
			return spawn_coordinates
		elif (spawn_point == "SW"):
			spawn_coordinates = [8,1]
			return spawn_coordinates
		elif (spawn_point == "SE"):
			spawn_coordinates = [8,8]
		return spawn_coordinates

def choose_hero(hero_class):

	print_slow(f"You have choosen the {hero_class}!")
	print_slow("Give your hero a name! ")

	hero_name = validate_str()
	validate(hero_name)

	if hero_class == "Knight":
		hero = Knight(hero_name)
	elif hero_class == "Wizard":
		hero = Wizard(hero_name)
	elif hero_class == "Rouge":
		hero = Rouge(hero_name)

	hero.print_stats()
	print_slow("-"*25)

	hero.add_hero_dict(dict_list)
	
	saved_character_list.append(hero)
	created_character_list.append(hero)
	save_character_to_json()
	#hero.score = 5

	choice = input("Press enter to continue or 9 to choose another Hero ")

	return choice, hero_name, hero
	#return hero


# Here starts the menu functions

def hero_menu():
	while True:
		clear_screen()
		hero_selected = False
		choice=0
		print_slow("-"*25)
		print_slow("Welcome to Dungeon run now it's time to choose your hero: ")
		print_slow("The available options are as follows :")
		print_slow("# 1 for Knight")
		print_slow("# 2 for Wizard")
		print_slow("# 3 for Rogue")
		print_slow("# 9 To Go Back")
		print_slow("-"*25)
		
		hero_select = validate_int()

		if (hero_select == 1):
			hero_selected = True
			choice, hero_name, hero = choose_hero("Knight")

		elif (hero_select == 2):
				hero_selected = True
				choice, hero_name = choose_hero("Wizard")

		elif (hero_select == 3):
				hero_selected = True
				choice, hero_name = choose_hero("Rouge")
		if choice == "9":
			continue
		if hero_select == 9:
			break
		if hero_selected is True:
			return True, hero_name, hero

def grid_menu():
	clear_screen()
	print_slow("-"*25)
	print_slow("A true hero needs a map to explore, please choose a grid size suitable for your adventure")
	print_slow("The available options are as follows :")
	print_slow("# 4 for 4x4 grid")
	print_slow("# 5 for 5x5 grid")
	print_slow("# 8 for 8x8 grid")
	print_slow("-"*25)
	try:
		grid_select = int(input('\n --> '))
	except ValueError:
		print("Bad input")

	if grid_select != 4 and grid_select != 5 and grid_select != 8:
		print_slow("Wrong input please follow the instructions correctly")
	else:
		return grid_select


def spawn_menu(grid_select):
	clear_screen()
	spawn_selected = False
	spawn_select = 0
	spawn_coordinates = []

	print_slow("-"*25)
	print_slow("Pick a spawn point on the map: ")
	print_slow("# 1 for NorthWest")
	print_slow("# 2 for NorthEast")
	print_slow("# 3 for SouthWest")
	print_slow("# 4 for SouthEast")
	print_slow("-"*25)

	try:
		spawn_select = int(input('\n --> '))
	except ValueError:
		print_slow("Wrong input")

	if spawn_select == 1:
		spawn_point = "NW"
		spawn_selected = True
		spawn_coordinates = [1, 1]
	elif spawn_select == 2:
		spawn_point = "NE"
		spawn_selected = True
		spawn_coordinates = calc_spawnpoint(grid_select,spawn_point)
	elif spawn_select == 3:
		spawn_point = "SW"
		spawn_selected = True
		spawn_coordinates = calc_spawnpoint(grid_select,spawn_point)
	elif spawn_select == 4:
		spawn_point = "SE"
		spawn_selected = True
		spawn_coordinates = calc_spawnpoint(grid_select,spawn_point)
	if spawn_selected:
		return spawn_coordinates

def check_if_outside(position,class_object):
	check_edge = class_object.get_room(position)
	if check_edge.edge is True:
		input("You left the map! Press enter to continue")
		game_loop = True
		return game_loop
		# skriv in vad som ska hända när man går utanför




def start_game(hero, grid_select, spawn_coordinates, hero_name):
	game_loop = False


	current_run = map(grid_size=grid_select)
	current_run.update_room(coordinate=spawn_coordinates, update="is_here")
	current_run.print_map()

	while game_loop is False:
		leave_or_not = ask_player_to_move(current_run, hero_name)
		clear_screen()
		current_run.print_map()
		position = current_run.where_am_i(option="return")
		game_loop = check_if_outside(position, current_run)
		x, y = position
		current_run.grid[y][x].fight_generator(hero)
		
	return

def ask_player_to_move(current_run, hero_name):
	print("# W to Move Up")
	print("# A to Move Left")
	print("# S to Move Down")
	print("# D to Move Right")
	print("# L to Save And Exit")
	

	move_choice= str(input("\n --> "))
	
	if (move_choice == "W"):
		movable_rooms = current_run.nerby_rooms()
		my_postiton = current_run.where_am_i()
		move_up= movable_rooms["above"]["coordinate"]
		current_run.update_room(coordinate=move_up, update="is_here")
		current_run.update_room(coordinate=my_postiton, update="finished")
		
	if (move_choice == "A"):
		movable_rooms = current_run.nerby_rooms()
		my_postiton = current_run.where_am_i()
		move_left= movable_rooms["left"]["coordinate"]
		current_run.update_room(coordinate=move_left, update="is_here")
		current_run.update_room(coordinate=my_postiton, update="finished")

	if (move_choice == "S"):
		movable_rooms = current_run.nerby_rooms()
		my_postiton = current_run.where_am_i()
		move_down= movable_rooms["below"]["coordinate"]
		current_run.update_room(coordinate=move_down, update="is_here")
		current_run.update_room(coordinate=my_postiton, update="finished")

	if (move_choice == "D"):
		movable_rooms = current_run.nerby_rooms()
		my_postiton = current_run.where_am_i()
		move_right= movable_rooms["right"]["coordinate"]
		current_run.update_room(coordinate=move_right, update="is_here")
		current_run.update_room(coordinate=my_postiton, update="finished")
		
		
	if (move_choice == "L"):
		ask_to_save(hero_name)
		# leave_loop = True
		# return leave_loop
		
#start_menu()
# grid_menu()
# hero_menu()
# spawn_menu()

if __name__ == "__main__":
	while True:
		grid_size = 0
		clear_screen()
		print_slow(" \n Dungeon Run \n")
		print_slow("-"*25)
		print_slow("# 1 New Game")
		print_slow("# 2 Load Game")
		print_slow("# 3 Quit")
		print_slow("-"*25)
		try:
			sub_meny = int(input('\n --> '))
		except ValueError:
			print_slow("Wrong input")
			continue

		if (sub_meny == 1):
			hero_name_status, hero_name, hero = hero_menu()
			if hero_name_status == True:
				grid_select = grid_menu()
				spawn_coordinates = spawn_menu(grid_select)
				start_game(hero, grid_select, spawn_coordinates, hero_name)
				


		elif (sub_meny == 2):
			hero_name_status, hero_name = load_hero()
			grid_select = grid_menu()
			spawn_coordinates = spawn_menu(grid_select)
			start_game(hero_name_status, grid_select, spawn_coordinates, hero_name)


		elif (sub_meny == 3):
			print_slow("BYEEEEEEEE")
			exit()