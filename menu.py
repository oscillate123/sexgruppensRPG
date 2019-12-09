from os import system, name
import sys, time
from map import map as m
from Monsters import *
from Hero import *
import json


with open("saved_heroes.json", "r") as open_file:
    dict_list = json.load(open_file)
    saved_heroes_list = []
    created_heroes_list = []
    for item in dict_list:
        if item["Type"] == "Knight":
            knight = Knight(item["Name"])
            knight.score = item["Score"]
            saved_heroes_list.append(knight)
        elif item["Type"] == "Wizard":
            wizard = Wizard(item["Name"])
            wizard.score = item["Score"]
            saved_heroes_list.append(wizard)
        elif item["Type"] == "Rouge":
            thief = Rouge(item["Name"])
            thief.score = item["Score"]
            saved_heroes_list.append(thief)


def save_character():
    if len(created_heroes_list) != 0:
        print("Created heroes: ")
        for item in created_heroes_list:
            print(item)
        print("Type in the name of the hero you want to save!")
        name_select = input("\n --> ")
        if name_select not in saved_heroes_list:
            #print(f"The hero {name_select} has already been saved!")
            for item in created_heroes_list:
                item = str(item)
                if name_select in item:
                    saved_heroes_list.append(item)
                    print("Hero saved!\n")
        with open("saved_heroes.json", "w") as close_file:
            json.dump(dict_list, close_file)
            close_file.close()
    else:
        print("A hero needs to be created in order to be saved!\n")


def load_hero():
    if len(saved_heroes_list) != 0:
        print("Saved heroes: \n")
        for item in saved_heroes_list:
            print(item)
        print("Write the name of the hero you want to play with!")
        name_select = input("\n --> ")
        for item in saved_heroes_list:
            item = str(item)
            if name_select in item:
                print(f"The hero '{name_select}' has been selected!")
            else:
                continue
                #print(f"No hero with the name '{name_select}' has been saved!")

    else:
        print("No heroes saved!")


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
            load_hero()


        elif (sub_meny == 3):
            save_character()


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
                    print_slow("Give your hero a name! ")
                    hero_name = input("\n --> ")
                    knight = Knight(hero_name)
                    print_slow("\nYour hero! \n")
                    knight.print_stats()
                    knight.add_hero_dict(dict_list)
                    created_heroes_list.append(knight)
                elif hero_select == 2:
                    hero_selected = True
                    print_slow("You have choosen the Thief! ")
                    print_slow("Give your hero a name!")
                    hero_name = input("\n --> ")
                    thief = Rouge(hero_name)
                    print_slow("\n Your hero!\n")
                    thief.print_stats()
                    thief.add_hero_dict(dict_list)
                    created_heroes_list.append(thief)
                elif hero_select == 3:
                    hero_selected = True
                    print_slow("You have choosen the Wizard! ")
                    print_slow("Give your hero a name! ")
                    hero_name = input("\n --> ")
                    wizard = Wizard(hero_name)
                    print_slow("\n Your hero!\n")
                    wizard.print_stats()
                    wizard.add_hero_dict(dict_list)
                    created_heroes_list.append(wizard)
                else:
                    print_slow("Wrong input! Please read the instructions")
                if hero_selected is True:
                    spawn_selected = False
                    clear_screen()
                    print_slow(" -----------------")
                    print_slow(f"You have now choosen your hero {hero_name} and you are ready for your adventure")
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
                elif spawn_select == 2:
                    spawn_point = "NE"
                    spawn_selected = True
                elif spawn_select == 3:
                    spawn_point = "SW"
                    spawn_selected = True
                elif spawn_select == 4:
                    spawn_point = "SE"
                    spawn_selected = True

                if spawn_selected == True:
                    print_slow(f"Your spawnpoint is {spawn_point}")
                    m.user_grid_req = grid_size
                    import map
                    # break



start_menu()