from os import system, name
import sys, time
from map import map as m
from Monsters import *
from Hero import *
import json


with open("saved_heroes.json", "r") as open_file:
    dict_list = json.load(open_file)
    saved_character_list = []
    created_character_list = []
    for item in dict_list:
        if item["Type"] == "Knight":
            knight = Knight(item["Name"])
            knight.score = item["Score"]
            saved_character_list.append(knight)


def save_character():
    with open("saved_heroes.json", "w") as close_file:
        json.dump(dict_list, close_file)
        close_file.close()


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


def start_menu():

    while True:
        clear_screen()
        grid_size = 0
        print_slow(" \n Dungeon Run \n")
        print_slow(" -----------------")
        print_slow(" #1 New Game")
        print_slow(" #2 Load Game")
        print_slow(" #3 Save Game")
        print_slow(" #4 Quit")

        print_slow(" -----------------")
        try:
            sub_meny = int(input('\n --> '))
        except ValueError:
            print_slow("Wrong input")
            continue

        if (sub_meny == 4):
            print_slow("BYEEEEEEEE")
            exit()

        elif (sub_meny == 2):

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
                  #  else:
                 #       break
                #print(f"No hero with the name '{name_select}' has been saved!")
            else:
                print("No heroes saved!")

        elif (sub_meny == 3):
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
                save_character()
                print("Hero saved!\n")
            else:
                print("A hero needs to be created in order to be saved!\n")

        elif (sub_meny == 1):
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
                grid_select = grid_size
                # return grid_size
                hero_selected = False
                hero_name = str
                clear_screen()
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
                    continue  # if(sub_meny == 1):

                if hero_select == 1:
                    hero_selected = True
                    print_slow("You have choosen the Knight! ")
                    print_slow("Give it a name! ")
                    hero_name = input("\n --> ")
                    knight = Knight(hero_name)
                    print_slow("\nYour hero! \n")
                    knight.print_stats()
                    knight.add_hero_dict(dict_list)
                    created_character_list.append(knight)
                    # hero_name = "Knight"
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
                if hero_selected is True:
                    spawn_selected = False
                    clear_screen()
                    print_slow(" -----------------")
                    print_slow(f"You have now choosen your hero:{hero_name} and you are ready for your adventure")
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
                    continue

                if spawn_select == 1:
                    spawn_point = "NW"
                    spawn_selected = True
                if spawn_select == 2:
                    spawn_point = "NE"
                    spawn_selected = True
                if spawn_select == 3:
                    spawn_point = "SW"
                    spawn_selected = True
                if spawn_select == 4:
                    spawn_point = "SE"
                    spawn_selected = True

                if spawn_selected == True:
                    print_slow(f"Your spawnpoint is {spawn_point}")
                    m.user_grid_req = grid_size
                    import map
                    # break



start_menu()