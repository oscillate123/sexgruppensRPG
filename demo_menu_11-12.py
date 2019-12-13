from os import system, name
import sys, time
from map import map as map
from Monsters import *
from Hero import *
import json
from pathlib import Path

folder = Path("json_file")
folder.mkdir(exist_ok=True)



#with open("json_file\saved_heroes.json","w+") as open_file:
	#if len(open_file.readlines()) == 0:
		#open_file.write("[]")
		#open_file.close()

with open("json_file\saved_heroes.json", "r") as open_file:
	dict_list = json.load(open_file)
	name_list = []
	saved_character_list = []
	created_character_list = []
	for dict in dict_list:
		# print(dict.keys())
		x = (dict.keys())
		y = list(x)
		name_list.append(y)
		#print(name_list)
		for heroes in dict:
			#print(dict.get(heroes).get("Type"))
			if (dict.get(heroes).get("Type")) == "Rouge":

				un= (dict.keys())
				for x in un:
					x = str(x)
					#print(x)
					rouge = Rouge(x)
				#rouge.score = dict.get("Score")
					#saved_character_list.append(rouge)
					
					#print(rouge.score)
				rouge.score = dict.get(heroes).get("Score")
				saved_character_list.append(rouge)

			elif (dict.get(heroes).get("Type")) == "Knight":

				un= (dict.keys())
				for x in un:
					x = str(x)
					#print(x)
					knight = Knight(x)
				#rouge.score = dict.get("Score")
					#saved_character_list.append(rouge)
					
					#print(rouge.score)
				knight.score = dict.get(heroes).get("Score")
				saved_character_list.append(knight)
			
			elif (dict.get(heroes).get("Type")) == "Wizard":

				un= (dict.keys())
				for x in un:
					x = str(x)
					#print(x)
					wizard = Wizard(x)
				#rouge.score = dict.get("Score")
					#saved_character_list.append(rouge)
					
					#print(rouge.score)
				wizard.score = dict.get(heroes).get("Score")
				saved_character_list.append(wizard)
				#print(rouge.score)
				#print(rouge)
				#input()

# if item["Type"] == "Knight":
# 		#	knight = Knight(item["Name"])
# 		#	knight.score = item["Score"]

			#for dict in heroes:
				#print(type(dict))
				#pass
	

	#for dict in dict_list:
		#print(dict.keys())
	#	x = (dict.keys())
	#	y = list(x)
	#	name_list.append(y)
	# for list in name_list:
	# 	name = str(list[0])
	# 	print(name)
	#for i in y:
	#	i = str(i)
	#	print(i)

	for dict in dict_list:
		pass
			#print(dict_list.get(dict))

			#if dict.get("Type") == "Rouge":
			#	print("JA BREEE")
			#	input()
			#print(dict.keys())

		#for item in dict:
		#if dict.get("Type") == "Rouge":
			#print("JA BREEE")
			#input()
			#rouge = Rouge(dict["Name"])

		#	rouge.score = dict["Score"]
		#if item["Type"] == "Knight":
		#	knight = Knight(item["Name"])
		#	knight.score = item["Score"]
		#if item["Type"] == "Wizard":
		#	wizard = Wizard(item["Name"])
		#	wizard.score = item["Score"]

#if dict.get("Type") == "Rouge":
		#	rouge = Rouge(dict["Name"])
		#	rouge.score = item["Score"]
		#	saved_character_list.append(rouge)
		#elif item["Type"] == "Knight":
		#	knight = Knight(item["Name"])
		#	knight.score = item["Score"]
		#	saved_character_list.append(knight)
		#elif item["Type"] == "Wizard":
		#	wizard = Wizard(item["Name"])
		#	wizard.score = item["Score"]
		#	saved_character_list.append(wizard)

		
# Here starts all the help functions for the program

def validation(hero_name):


def clear_screen():
	if name == 'nt':
		_ = system('cls')
	# else:
	# 	_ = system('clear')

def print_slow(str):
	str = str + "\n"
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.02)

def load_hero():
	if len(saved_character_list) != 0:
		print("Saved heroes: \n")
		#print(saved_character_list)
		for item in saved_character_list:
			print(item)
		print("Write the name of the hero you want to play with!")
		name_select = input("\n --> ")
		for item in saved_character_list:
			item = str(item)
			if name_select in item:
				for item in dict_list:
					#print(item.keys())
					un= (item.keys())
					for name in un:
						name = str(name)
						if name == name_select:
							#print("true")
							#item=dict(item)
							#dpp=item.get("name_select").get("Type")
							#input()
							#print(item.get(name).get("Type"))
							if item.get(name).get("Type") == "Knight":
								#print("true")

								knight = Knight(name)
								knight.score = item.get(name).get("Score")
								print(knight)
								print(knight.score)
							elif item.get(name).get("Type") == "Wizard":
								#print("true")

								wizard = Wizard(name)
								wizard.score = item.get(name).get("Score")
								print(wizard)
								print(wizard.score)
							elif item.get(name).get("Type") == "Rouge":
								#print("true")

								rouge = Rouge(name)
								rouge.score = item.get(name).get("Score")
								print(rouge)
								print(rouge.score)


				print(f"The hero '{name_select}' has been selected!")
				print_slow(" -----------------")
				input("Press enter to continue")
			#  else:
			#       break
		#print(f"No hero with the name '{name_select}' has been saved!")
	else:
		print("No heroes saved!")
		start_menu()

def save_character_to_json():
	with open("json_file\saved_heroes.json", "w+") as close_file:
		close_file.seek(0)
		close_file.truncate()
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
			start_menu()
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
			spawn_point = spawn_menu()
		elif (sub_meny == 2):
			load_hero()
			grid_select = grid_menu()
			spawn_point = spawn_menu()

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
			#for name in dict_list:
			#	name = str(name)
			#	print(name)
			#	if hero_name in name:
			#		print(hero_name)
			#		print(name)

		for item in dict_list:
			# print(item.keys())
			un = (item.keys())
			for name in un:
				name = str(name)
				if name == hero_name:
					lala = True
					while lala == True:
						print_slow("Name already in use!")
						print_slow("We will rerun the hero option so please choose a name that is not already in the list")
						#input("Press enter if you can read english and understood the message above!")
						print("Give your hero name")
						hero_name = input("\n --> ")
						if hero_name != name:
							break
						#hero_menu()
						# break
						#hero_selected = False

				else:
					continue


		knight = Knight(hero_name)
		knight.print_stats()
		knight.add_hero_dict(dict_list)
		print_slow(" -----------------")
		input("Press enter to continue")
		created_character_list.append(knight)

	elif (hero_select == 2):
		hero_selected = True
		print_slow("You have choosen the Rogue! ")
		print_slow("Give your hero a name! ")
		hero_name = input("\n --> ")
		rouge = Rouge(hero_name)
		#if hero_name in item in saved_character_list:
			#print("Choose another name")
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

def spawn_menu():
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
		current_run.update_current_cuboid(coordinate=spawn_coordinates)
		map_object = current_run.check_cuboid(coordinate=current_run.current_cuboid, option='return')
		print_slow(f"Your spawnpoint is on the {map_object}, at coordinate {current_run.current_cuboid}")
		current_run.print_map()
		ask_to_save()
		input()# start game
		#return current_run


start_menu()
# grid_menu()
# hero_menu()
# spawn_menu()11
