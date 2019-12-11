from os import system, name
import sys, time
from map import map as map
from Monsters import *
from Hero import *
import json


with open("saved_heroes.json","r") as open_file:
	dict_list = json.load(open_file)
	saved_character_list = []
	created_character_list = []
	for item in dict_list:
		if item["Type"] == "Rouge":
			rouge = Rouge(item["Name"])
			rouge.score = item["Score"]
			saved_character_list.append(rouge)
		elif item["Type"] == "Knight":
			knight = Knight(item["Name"])
			knight.score = item["Score"]
			saved_character_list.append(knight)
		elif item["Type"] == "Wizard":
			wizard = Wizard(item["Name"])
			wizard.score = item["Score"]
			saved_character_list.append(wizard)

		
# Here starts all the help functions for the program

def clear_screen():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

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
				print(f"The hero '{name_select}' has been selected!")
				print_slow(" -----------------")
				input("Press enter to continue")
		
	else:
		print("No heroes saved!")

def save_character_to_json():
    with open("saved_heroes.json", "w") as close_file:
        json.dump(dict_list, close_file)
        close_file.close()

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
				saved_character_list.append(item)
			save_character_to_json()
			print("Hero saved!\n")
	else:
		print("A hero needs to be created in order to be saved!\n")

def ask_to_save():
	print_slow(" do you want to save your character at this point?")
	print_slow("# 1 Save")
	print_slow("# 2 Continue exploring")
	try:
		answer = int(input('\n --> '))
	except ValueError:
		print_slow("Wrong input")
	if (answer == 1):
		save_character()
	else:
		return

def calc_spawnpoint(grid_select,spawn_point):
	# det funktion räknar ut vilken spawn_coordinate du kmr spawna på oavsett vilket gridsize du väljer
	# bara att om man väljer 8x8 grid och väljer "NE"[9,9] så skriver den ut att det blir "None" i programmet
	spawn_coordinates = []
	if grid_select == 4:
		if (spawn_point == "NE"):
			spawn_coordinates = [0,5]
			return spawn_coordinates
		elif (spawn_point == "SW"):
			spawn_coordinates = [5,0]
			return spawn_coordinates
		elif (spawn_point == "NE"):
			spawn_coordinates = [5,5]
			return spawn_coordinates
	if (grid_select==5):
		if (spawn_point == "NE"):
			spawn_coordinates = [0,6]
			return spawn_coordinates
		elif (spawn_point == "SW"):
			spawn_coordinates = [6,0]
			return spawn_coordinates
		elif (spawn_point == "NE"):
			spawn_coordinates = [6,6]
			return spawn_coordinates
	if (grid_select==8):
		if (spawn_point == "NE"):
			spawn_coordinates = [0,9]
			return spawn_coordinates
		elif (spawn_point == "SW"):
			spawn_coordinates = [9,0]
			return spawn_coordinates
		elif (spawn_point == "NE"):
			spawn_coordinates = [9,9]
			return spawn_coordinates



# Here starts the menu functions


def start_menu():
	while True:
		grid_size = 0
		clear_screen()
		print_slow(" \n Dungeon Run \n")
		print_slow(" -----------------")
		print_slow("# 1 New Game")
		print_slow("# 2 Load Game")
		print_slow("# 3 Quit")
		print_slow(" -----------------")
		try:
			sub_meny = int(input('\n --> '))
		except ValueError:
			print_slow("Wrong input")
			continue

		if (sub_meny == 1):
			hero_name = hero_menu()
			grid_select = grid_menu()
			spawn_coordinates = spawn_menu(grid_select)
			start_game(hero_name, grid_select, spawn_coordinates)
		elif (sub_meny == 2):
			load_hero()
			grid_select = grid_menu()
			spawn_coordinates = spawn_menu(grid_select)

		elif (sub_meny == 3):
			print_slow("BYEEEEEEEE")
			exit()


def grid_menu():
	clear_screen()
	print_slow(" -----------------")
	print_slow("A true hero needs a map to explore, please choose a grid size suitable for your adventure")
	print_slow("The available options are as follows :")
	print_slow("# 4 for 4x4 grid")
	print_slow("# 5 for 5x5 grid")
	print_slow("# 8 for 8x8 grid")
	print_slow(" -----------------")
	grid_select = int(input('\n --> '))
	if grid_select != 4 and grid_select != 5 and grid_select != 8:
		print_slow("Wrong input please follow the instructions correctly")
	else:
		return grid_select


def hero_menu():
	clear_screen()
	hero_selected = False
	hero_name = str
	print_slow(" -----------------")
	print_slow("Welcome to Dungeon run now it's time to choose your hero: ")
	print_slow("The available options are as follows :")
	print_slow("# 1 for Knight")
	print_slow("# 2 for Rogue")
	print_slow("# 3 for Wizard")
	print_slow(" -----------------")
	try:
		hero_select = int(input('\n --> '))
	except ValueError:
		print_slow("Wrong input")

	if (hero_select == 1):
		hero_selected = True
		print_slow("You have choosen the Knight! ")
		print_slow("Give your hero a name! ")
		hero_name = input("\n --> ")
		knight = Knight(hero_name)
		knight.print_stats()
		print_slow(" -----------------")
		input("Press enter to continue")
		knight.add_hero_dict(dict_list)
		created_character_list.append(knight)

	elif (hero_select == 2):
		hero_selected = True
		print_slow("You have choosen the Rogue! ")
		print_slow("Give your hero a name! ")
		hero_name = input("\n --> ")
		rouge = Rouge(hero_name)
		rouge.print_stats()
		print_slow(" -----------------")
		input("Press enter to continue")
		rouge.add_hero_dict(dict_list)
		created_character_list.append(rouge)
	elif (hero_select == 3):
		hero_selected = True
		print_slow("You have choosen the Wizard! ")
		print_slow("Give your hero a name! ")
		hero_name = input("\n --> ")
		wizard = Wizard(hero_name)
		wizard.print_stats()
		print_slow(" -----------------")
		input("Press enter to continue")
		wizard.add_hero_dict(dict_list)
		created_character_list.append(wizard)
		
	else:
		print_slow("Wrong input! Please read the instructions")
	if hero_selected is True:
		return hero_name

def spawn_menu(grid_select):
	clear_screen()
	spawn_selected = False
	spawn_select = 0
	spawn_coordinates = []

	print_slow(" -----------------")
	print_slow("Pick a spawn point on the map: ")
	print_slow("# 1 for NorthWest")
	print_slow("# 2 for NorthEast")
	print_slow("# 3 for SouthWest")
	print_slow("# 4 for SouthEast")
	print_slow(" -----------------")

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


# gjorde en funktion för spelet. så vi kan skicka med den info vi behöhver från ovanstående meny funktioner
# map sizen ändrar nu med spelarens val av size
# men man kan inte gå mer en ett steg i spelet. och den lägger bara till fler x på samma plats. (dvs klarade inte det oscar bad mig att göra xxdxddxx /emil)

def start_game(hero_name, grid_select, spawn_coordinates):
	game_loop = False
	current_run = map(name="demo_run",grid_size= grid_select)
	current_run.cuboid_character_handler(new_character=current_run.mark_character, option="mark", coordinate=current_run.current_cuboid)
	print_slow(f"Your spawnpoint is at coordinate {spawn_coordinates}")
	current_run.print_map()

	while game_loop is False:
		leave_or_not = ask_player_to_move(current_run)
		if leave_or_not is True:
			break	
		current_run.print_map()
		
		

	input()# start game
	#return current_run

"""

	nerby_cubids_data = game.get_nerby_cuboids()

	user_move = input("Where you wanna go? (above, below, right, left)")

	new_cuboid = nerby_cubids_data[f"{user_move}"]["coordinate"]
	
	game.update_current_cuboid(old_coordinate=game.current_cuboid, option='move', new_coordinate=new_cuboid)

"""

def ask_player_to_move(current_run):
	print_slow("# W to Move Up")
	print_slow("# A to Move Left")
	print_slow("# S to Move Down")
	print_slow("# D to Move Right")
	print_slow("# L to Leave Game")
	print_slow("# K to Save Game")

	move_choice= str(input("\n --> "))
	
	if (move_choice == "W"):
		user_direction = "above"
		nerby_cubids_data = current_run.get_nerby_cuboids()
		new_cuboid_coordinate = nerby_cubids_data[user_direction]["coordinate"]
		current_run.update_current_cuboid(old_coordinate=current_run.current_cuboid,
										  option="move",
										  new_coordinate=new_cuboid_coordinate)
		
	if (move_choice == "A"):
		user_direction = "left"
		nerby_cubids_data = current_run.get_nerby_cuboids()
		new_cuboid_coordinate = nerby_cubids_data[user_direction]["coordinate"]
		current_run.update_current_cuboid(old_coordinate=current_run.current_cuboid,
										  option="move",
										  new_coordinate=new_cuboid_coordinate)
	if (move_choice == "S"):
		user_direction = "below"
		nerby_cubids_data = current_run.get_nerby_cuboids()
		new_cuboid_coordinate = nerby_cubids_data[user_direction]["coordinate"]
		current_run.update_current_cuboid(old_coordinate=current_run.current_cuboid,
										  option="move",
										  new_coordinate=new_cuboid_coordinate)
	if (move_choice == "D"):
		user_direction = "right"
		nerby_cubids_data = current_run.get_nerby_cuboids()
		new_cuboid_coordinate = nerby_cubids_data[user_direction]["coordinate"]
		current_run.update_current_cuboid(old_coordinate=current_run.current_cuboid,
										  option="move",
										  new_coordinate=new_cuboid_coordinate)
	if (move_choice == "L"):
		leave_loop = True
		return leave_loop
		#end game loop
	if (move_choice == "K"):
		ask_to_save()
		
	



start_menu()
# grid_menu()
# hero_menu()
# spawn_menu()
