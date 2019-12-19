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
from colors import *

#maximize_console()
#activate before compiling to .exe
os.system('color 02')

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
		dict_list = {}
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
		print_slow("Saved heroes: \n")
		for item in saved_character_list:
			item = str(item)
			print_slow(item)
		print_slow("Write the name of the hero you want to play with!")
		name_select = input("\n --> ")
		for item in saved_character_list:
			item = str(item)
			if name_select in item:
					dict_keys= (dict_list.keys())
					for name in dict_keys:
						name = str(name)
						if name == name_select:
							if dict_list[name]["Type"] == "Knight":
								hero = Knight(name)
								hero.score_list.append(dict_list[name]["Score"]) 
								#created_character_list.append(Knight(name))
								#print_slow(created_character_list)

								
								
								

							elif dict_list[name]["Type"] == "Wizard":
								hero = Wizard(name)
								hero.score_list.append(dict_list[name]["Score"])
							elif dict_list[name]["Type"] == "Rouge":
								hero = Rouge(name)
								hero.score_list.append(dict_list[name]["Score"])
		saved_character_list.append(hero)
		print_slow(f"The hero '{name_select}' has been selected!")
		print_slow("-"*20)
		input("Press enter to continue")
		return True, name_select, hero
	else:
		print_slow("No heroes saved!")
		input("Press enter to continue and create a new hero")
		status, hero_name, hero_instance = hero_menu()
		return	status, hero_name, hero_instance

def save_character_to_json():
	with open("json_file/saved_heroes.json", "w+") as close_file:
		close_file.seek(0)
		close_file.truncate()
		json.dump(dict_list, close_file)
		close_file.close()

def update_score(hero_name, instance):
	x	= sum(instance.score_list)
	x = int(x)
	print_slow("Your total score is: " + "{}".format(x))
	print_slow_but_fast("Autosaving...")
	time_now = time.strftime("%m/%d Time %H:%M")
	dict_list[hero_name]["Score"] = x
	dict_list[hero_name]["Time"] = time_now
	saved_character_list[saved_character_list.index(instance)] = instance
	save_character_to_json()
	print_slow_but_fast("Autosave done")	

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

def ask_to_save(hero_name,score,hero):
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
				
				update_score(item.hero_name,score,item)
			# else:
			# 	print_slow("Couldn't save")
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
	#created_character_list.append(hero)
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
			choice, hero_name, hero_instance = choose_hero("Knight")

		elif (hero_select == 2):
				hero_selected = True
				choice, hero_name, hero_instance = choose_hero("Wizard")

		elif (hero_select == 3):
				hero_selected = True
				choice, hero_name, hero_instance = choose_hero("Rouge")
		if choice == "9":
			continue
		if hero_select == 9:
			return False, "hero_name", "hero_instance" 
		if hero_selected is True:
			return True, hero_name, hero_instance

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
		print_slow("Bad input")

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
		return False
		# skriv in vad som ska hända när man går utanför
	else:
		game_loop = True
		return game_loop




def start_game(hero, grid_select, spawn_coordinates, hero_name, oscars_hotfix):
	game_loop = True


	current_run = map(grid_size=grid_select)
	current_run.update_room(coordinate=spawn_coordinates, update="is_here")
	current_run.print_map()

	while game_loop is True:
		old_position = ask_player_to_move(current_run, hero_name)

		clear_screen()

		current_run.print_map()

		position = current_run.where_am_i(option="return")
		is_not_outside = check_if_outside(position, current_run) # returns True for not outside and False for is outside

		if not is_not_outside: # if not True/False, outside of map == False
			return "end"

		x, y = position

		current_room = current_run.grid[y][x]

		if oscars_hotfix == 0: # om det är första rundan i spelet så kommer den att sätta första rummet som neutraliserat
			current_room.fight == False
			oscars_hotfix += 1

		if current_room.fight == False:
			# if the room is already "finished" or if it is "edge", if edge should be picked up a few lines above doe
			fight_outcome = "win" # this is only so it will go down a few lines into the "elif  fight_outcome == "win":" section
		else:
			# if the room is "unfinished" or "untouched"
			current_fight = current_run.grid[y][x].fight_generator(hero) # genererar en fight instans för dem x,y coordinates som anges
			fight_outcome = current_fight.run_fight() # kör den fighteninstansen och ska returnera outcome för fighten

		# försöka få mapen att uppdatera sig utifrån hur fight outcome blir
		if fight_outcome == "escaped":
			current_run.update_room(coordinate=old_position, update="unfinished")
		elif  fight_outcome == "win":
			score = current_room.total_loot
			hero.score_list.append(score)
			print("Your points from this round: {}".format(score))
			update_score(hero_name, hero)
			current_room.total_loot = 0
			current_room.fight = False
		elif fight_outcome == "died":
			break

		current_run.print_map()
		
	
	return

def ask_player_to_move(current_run, hero_name):
	
	print("# W to Move Up")
	print("# A to Move Left")
	print("# S to Move Down")
	print("# D to Move Right")
	print("# L Exit")
	

	move_choice= str(input("\n --> "))
	
	if (move_choice == "W"):
		movable_rooms = current_run.nerby_rooms()
		my_postiton = current_run.where_am_i()
		move_up= movable_rooms["above"]["coordinate"]
		current_run.update_room(coordinate=move_up, update="is_here")
		current_run.update_room(coordinate=my_postiton, update="finished")
		return my_postiton
		
	elif (move_choice == "A"):
		movable_rooms = current_run.nerby_rooms()
		my_postiton = current_run.where_am_i()
		move_left= movable_rooms["left"]["coordinate"]
		current_run.update_room(coordinate=move_left, update="is_here")
		current_run.update_room(coordinate=my_postiton, update="finished")
		return my_postiton
	elif (move_choice == "S"):
		movable_rooms = current_run.nerby_rooms()
		my_postiton = current_run.where_am_i()
		move_down= movable_rooms["below"]["coordinate"]
		current_run.update_room(coordinate=move_down, update="is_here")
		current_run.update_room(coordinate=my_postiton, update="finished")
		return my_postiton

	elif (move_choice == "D"):
		movable_rooms = current_run.nerby_rooms()
		my_postiton = current_run.where_am_i()
		move_right= movable_rooms["right"]["coordinate"]
		current_run.update_room(coordinate=move_right, update="is_here")
		current_run.update_room(coordinate=my_postiton, update="finished")
		return my_postiton
		
	elif (move_choice == "L"):
		print_slow("Who are you kidding we know you have nothing else to do")
		time.sleep(3)
		exit()


#start_menu()
# grid_menu()
# hero_menu()
# spawn_menu()

if __name__ == "__main__":

	oscars_hotfix = 0

	while True:
		grid_size = 0
		clear_screen()
		print_slow_but_fast("""


				██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗    ██████╗ ██╗   ██╗███╗   ██╗
				██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║    ██╔══██╗██║   ██║████╗  ██║
				██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║    ██████╔╝██║   ██║██╔██╗ ██║
				██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║    ██╔══██╗██║   ██║██║╚██╗██║
				██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║    ██║  ██║╚██████╔╝██║ ╚████║
				╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
																								

		""")
		#print_slow(" \n Dungeon Run \n")
		print_slow_but_fast("-"*50 + "Welcome to DUNGEON RUN choose an option to continue" + "-"*50)
		print_slow_but_fast(" "*65+"-"*15)
		#print_slow("Welcome to DUNGEON RUN choose an option to go continue")
		print_slow_but_fast(" "*65+"# 1 New Game")
		print_slow_but_fast(" "*65+"# 2 Load Game")
		print_slow_but_fast(" "*65+"# 3 Quit")
		print_slow_but_fast(" "*65+"-"*15)
		try:
			sub_meny = int(input("\n"+" "*65+"-->"))
		except ValueError:
			print_slow("Wrong input")
			continue

		if (sub_meny == 1):
			hero_name_status, hero_name, hero_instance = hero_menu()
			if hero_name_status == True:
				grid_select = grid_menu()
				spawn_coordinates = spawn_menu(grid_select)
				the_game = start_game(hero_instance, grid_select, spawn_coordinates, hero_name, oscars_hotfix)
				if the_game == "end":
					continue
				else:
					input("You died, now returning to main menu. Press enter to continue")
				continue
				
		elif (sub_meny == 2):
			hero_name_status, hero_name, hero_instance = load_hero()
			grid_select = grid_menu()
			spawn_coordinates = spawn_menu(grid_select)
			the_game = start_game(hero_instance, grid_select, spawn_coordinates, hero_name, oscars_hotfix)
			if the_game == "end":
				continue
			else:
				input("You died, now returning to main menu. Press enter to continue")
			continue

		elif (sub_meny == 3):
			print_slow("If you refer a friend, you will unlock a special character. Cya!")
			exit()