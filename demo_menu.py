from os import system, name
import sys, time
from map import map as map
from Monsters import *
from Hero import *
import json
from other_functions import *


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
				return name_select
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

			saved_character_list.append(item)
			save_character_to_json()
			print("Hero saved!\n")
	else:
		print("A hero needs to be created in order to be saved!\n")

def ask_to_save():
	print_slow(" Do you want to save your character at this point?")
	print_slow("# 1 Save")
	print_slow("# 2 To Exit Game")
	try:
		answer = int(input('\n --> '))
	except ValueError:
		print_slow("Wrong input")
	if (answer == 1):
		save_character()
	else:
		print_slow("Thanks for playing Dungeon Run!")
		print_slow("Created by: Robert, Sadri, Oliver, Oscar and Emil")
		exit()

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

def choose_hero(hero_class):

    print_slow(f"You have choosen the {hero_class}!")
    print_slow("Give your hero a name! ")

    hero_name = validate_str()

    if hero_class == "Knight":
        hero = Knight(hero_name)
    if hero_class == "Wizard":
        hero = Wizard(hero_name)
    if hero_class == "Rouge":
        hero = Rouge(hero_name)

    hero.print_stats()
    print_slow(" -----------------")

    hero.add_hero_dict(dict_list)
    
    created_character_list.append(hero)

    choice = input("Press enter to continue or 9 to choose another Hero ")

    return choice


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
			if hero_name == True:
				grid_select = grid_menu()
				spawn_coordinates = spawn_menu(grid_select)
				start_game(hero_name, grid_select, spawn_coordinates)
				


		elif (sub_meny == 2):
			hero_name = load_hero()
			grid_select = grid_menu()
			spawn_coordinates = spawn_menu(grid_select)
			start_game(hero_name, grid_select, spawn_coordinates)


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
	while True:
		clear_screen()
		hero_selected = False
		choice=0
		print_slow(" -----------------")
		print_slow("Welcome to Dungeon run now it's time to choose your hero: ")
		print_slow("The available options are as follows :")
		print_slow("# 1 for Knight")
		print_slow("# 2 for Rogue")
		print_slow("# 3 for Wizard")
		print_slow("# 9 To Go Back")
		print_slow(" -----------------")
		
		hero_select = validate_int()

		if (hero_select == 1):
			hero_selected = True
			choice = choose_hero("Knight")

		elif (hero_select == 2):
				hero_selected = True
				choice = choose_hero("Wizard")

		elif (hero_select == 3):
				hero_selected = True
				choice = choose_hero("Rouge")
		if choice == "9":
			continue
		if hero_select == 9:
			break
		if hero_selected is True:
			return True

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
	print_slow("# L to Save And Exit")
	

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
		ask_to_save()
		leave_loop = True
		return leave_loop
		#end game loop

	



start_menu()
# grid_menu()
# hero_menu()
# spawn_menu()
