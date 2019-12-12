from os import system, name
import sys, time
from map import map as map
from Monsters import *
from Hero import *
import json
from other_functions import*

created_character_list = []

with open("saved_heroes.json", "r") as open_file:
    dict_list = json.load(open_file)
    saved_character_list = []
    created_character_list = []

    for item in dict_list:
        if item["Type"] == "Knight":
            knight = Knight(item["Name"])
            knight.score = item["Score"]
            saved_character_list.append(knight)

with open("saved_heroes.json","r") as open_file:
	dict_list = json.load(open_file)
	saved_character_list = []
	created_character_list = []

	for item in dict_list:
		if item["Type"] == "Rouge":
			rouge = Rouge(item["Name"])
			rouge.score = item["Score"]
			saved_character_list.append(rouge)

def load_hero():
    if len(saved_character_list) != 0:
        print("Saved heroes: \n")

        for item in saved_character_list:
            print(item)
        print("Write the name of the hero you want to play with!")

        name_select = validate_str()

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

        sub_meny = validate_int()

        if (sub_meny == 1):
            hero_name = hero_menu()

            if hero_name == True:
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
    grid_selected = False

    while(grid_selected == False):
        clear_screen()
        print_slow(" -----------------")
        print_slow("A true hero needs a map to explore, please choose a grid size suitable for your adventure")
        print_slow("The available options are as follows :")
        print_slow("# 4 for 4x4 grid")
        print_slow("# 5 for 5x5 grid")
        print_slow("# 8 for 8x8 grid")
        print_slow(" -----------------")
        grid_select = validate_int()

        if grid_select is 4 or grid_select is 5 or grid_select is 8:
            return grid_select

def save_character():
    if len(created_character_list) != 0:

        for item in created_character_list:
            saved_character_list.append(item)
            print(item)

        save_character_to_json()
        print("Hero saved!\n")

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
    print(dict_list)
    created_character_list.append(hero)

    choice = input("Press enter to continue or 9 to choose another Hero ")

    return choice

def hero_menu():
    while(True):
        clear_screen()
        hero_selected = False
        choice = 0
        hero_name = ""
        print_slow(" -----------------")
        print_slow("Welcome to Dungeon run now it's time to choose your hero: ")
        print_slow("The available options are as follows :")
        print_slow("# 1 for Knight")
        print_slow("# 2 for Wizard")
        print_slow("# 3 for Rouge")
        print_slow("# 9 Back to main meny")
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

        #Nödlösning med en int och str orkade inte mer...
        if choice == '9':
            continue

        if hero_select == 9:
            break

        if hero_selected is True:
            return True

def spawn_menu():
    spawn_selected = False

    while(spawn_selected == False):
        clear_screen()
        spawn_select = 0
        spawn_coordinates = []

        print_slow(" -----------------")
        print_slow("Pick a spawn point on the map: ")
        print_slow("# 1 for NorthWest")
        print_slow("# 2 for NorthEast")
        print_slow("# 3 for SouthWest")
        print_slow("# 4 for SouthEast")
        print_slow(" -----------------")

        spawn_select = validate_int()

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
        else:
            print("Wrong choice")
            continue

    if spawn_selected:
        current_run = map(name="demo_run")
        current_run.update_current_cuboid(coordinate=spawn_coordinates)
        map_object = current_run.check_cuboid(coordinate=current_run.current_cuboid, option='return')
        print_slow(f"Your spawnpoint is on the {map_object}, at coordinate {current_run.current_cuboid}")
        current_run.print_map()
        save_character()
        input()

if __name__ == "__main__":
    start_menu()