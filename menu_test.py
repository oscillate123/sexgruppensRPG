def start_menu():
    while True:
        grid_size = 0
        print(" \n Dungeon Run \n")
        print(" -----------------")
        print(" #1 New Game")
        print(" #2 Load Game")
        print(" #3 Quit")
        print(" -----------------")
        try:
           sub_meny = int(input('\n --> '))
        except ValueError:
            print("Wrong input")
            continue
    
        if (sub_meny ==1):
            grid_select = grid_menu()
            hero_name,player_name = hero_menu()
            spawn_point = spawn_menu()
        if (sub_meny == 2):
            pass
        if (sub_meny ==3):
            print("BYEEEEEEEE")
            exit()

def grid_menu():
    print(" -----------------")
    print("Welcome to the new game now it's time to choose the grid size:")
    print("The available options are as follows :")
    print("# 4 for 4x4 grid")
    print("# 5 for 5x5 grid")
    print("# 8 for 8x8 grid")
    print(" -----------------")
    grid_select = int(input('\n --> '))
    if grid_select != 4 and grid_select != 5 and grid_select != 8:
        print("Wrong input please follow the instructions correctly")
    else:
        return grid_select

def hero_menu():
    hero_selected = False
    hero_name = str
    print(" -----------------")
    print("Welcome to the grid now it's time to choose your hero: ")
    print("The available options are as follows :")
    print("# 1 for Knight")
    print("# 2 for Thief")
    print("# 3 for Magician")
    print(" -----------------")
    try:
        hero_select = int(input('\n --> '))
    except ValueError:
        print("Wrong input")
         
    if hero_select == 1:
        hero_selected = True
        print("You have choosen the Knight! ")
        hero_name = "Knight"
        #print knight.stats()
    elif hero_select == 2:
        hero_selected = True
        print("you have choosen the Thief! ")
        hero_name = "Thief"        
        #print thief.stats()
    elif hero_select == 3:
        hero_selected = True
        print("you have choosen the Magician! ")
        hero_name = "Magician" 
            #print magician.stats()
    else:
        print("Wrong input! Please read the instructions")
    if hero_selected is True:
        try:
            print(f"You have now choosen your hero:{hero_name}. Now your hero needs a name!")
            player_name = str(input('\n --> '))
        except ValueError:
            print("Wrong input")
            
        return hero_name,player_name

def spawn_menu():
    spawn_selected=False
    print(" -----------------")
    print("Pick a spawn point on the map: ")
    print("# 1 for NorthWest")
    print("# 2 for NorthEast")
    print("# 3 for SouthWest")
    print("# 4 for SouthEast")
    print(" -----------------")
    try:
        spawn_select = int(input('\n --> '))
    except ValueError:
        print("Wrong input")
        
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
        print(f"Your spawnpoint is {spawn_point}")
        #start game
        return spawn_point

start_menu()
        