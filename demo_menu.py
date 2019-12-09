from os import system, name
import sys, time
from map import map as map


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
		time.sleep(0.05)


def start_menu():
	while True:
		grid_size = 0
		clear_screen()
		print_slow(" \n Dungeon Run \n")
		print_slow(" -----------------")
		print_slow(" #1 New Game")
		print_slow(" #2 Load Game")
		print_slow(" #3 Quit")
		print_slow(" -----------------")
		try:
			sub_meny = int(input('\n --> '))
		except ValueError:
			print_slow("Wrong input")
			continue

		if (sub_meny == 1):
			grid_select = grid_menu()
			hero_name, player_name = hero_menu()
			spawn_point = spawn_menu()
		elif (sub_meny == 2):
			pass
		elif (sub_meny == 3):
			print_slow("BYEEEEEEEE")
			exit()


def grid_menu():
	clear_screen()
	print_slow(" -----------------")
	print_slow("Welcome to the new game now it's time to choose the grid size:")
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

hero_selected = False
def hero_menu():
	clear_screen()
	#hero_selected = False
	hero_name = str
	print_slow(" -----------------")
	print_slow("Welcome to the grid now it's time to choose your hero: ")
	print_slow("The available options are as follows :")
	print_slow("# 1 for Knight")
	print_slow("# 2 for Thief")
	print_slow("# 3 for Magician")
	print_slow(" -----------------")
	try:
		hero_select = int(input('\n --> '))
	except ValueError:
		print_slow("Wrong input")

	if hero_select == 1:
		hero_selected = True
		print_slow("You have choosen the Knight! ")
		hero_name = "Knight"
		# print_slow knight.stats()
	elif hero_select == 2:
		hero_selected = True
		print_slow("you have choosen the Thief! ")
		hero_name = "Thief"
		# print_slow thief.stats()
	elif hero_select == 3:
		hero_selected = True
		print_slow("you have choosen the Magician! ")
		hero_name = "Magician"
		# print_slow magician.stats()
	else:
		print_slow("Wrong input! Please read the instructions")
	if hero_selected == True:
		try:
			print_slow(f"You have now choosen your hero {hero_name}. Now your hero needs a name!")
			print_slow("Type in the name that you want to use:")
			player_name = str(input('\n --> '))
		except ValueError:
			print_slow("Wrong input")

		return hero_name, player_name


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
		input()# start game
		#return current_run


start_menu()
# grid_menu()
# hero_menu()
# spawn_menu()11
