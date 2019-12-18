from os import system, name
import sys, time

def validate_int():
    while True:
        try:
            age = int(input("\n --> "))
        except ValueError:
            print("Wrong format, try again.")
            continue
        else:
            return age

def validate_str():
    while True:
        name = input("\n --> ")

        if name.isalpha() or name == "":
            hero_name = name.lower().capitalize()
            return hero_name 
        else:
            print("Wrong format, try again.")
            continue

def validate_name():
    while True:
        name = input("\n --> ")

        if name.isalpha():
            return name.lower().capitalize()
        else:
            print("Wrong format, try again.")
            continue


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
		time.sleep(0.001)

def print_slow_but_fast(str):
	str = str + "\n"
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.0000001)

def game_over_screen():
    print_slow_but_fast("""

                                    
                ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          



    """)
    print_slow_but_fast("""
    

        ██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ███████╗ █████╗ ██████╗     ███╗   ███╗ ██████╗ ██╗  ██╗████████╗███████╗██████╗ ███████╗                  ███████╗██████╗ 
        ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔════╝██╔══██╗██╔══██╗    ████╗ ████║██╔═══██╗██║  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝▄ ██╗▄▄ ██╗▄▄ ██╗▄██╔════╝██╔══██╗
         ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║█████╗  ███████║██║  ██║    ██╔████╔██║██║   ██║███████║   ██║   █████╗  ██████╔╝█████╗   ████╗ ████╗ ████╗█████╗  ██████╔╝
          ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██╔══╝  ██╔══██║██║  ██║    ██║╚██╔╝██║██║   ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗██╔══╝  ▀╚██╔▀▀╚██╔▀▀╚██╔▀██╔══╝  ██╔══██╗
           ██║   ╚██████╔╝╚██████╔╝    ██████╔╝███████╗██║  ██║██████╔╝    ██║ ╚═╝ ██║╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║██║       ╚═╝   ╚═╝   ╚═╝ ███████╗██║  ██║
           ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝                       ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                  

    """)



if __name__ == "__main__":
    pass
    #hej2 = validate_int()
    #hej3 = validate_str()
    #print(validate_name())