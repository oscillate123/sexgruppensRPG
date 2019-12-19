from os import system, name
import sys, time
import os
import ctypes
import msvcrt
import subprocess
from ctypes import wintypes


kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

def maximize_console(lines=None):
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)


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
		time.sleep(0.01)

def print_slow_but_fast(str):
	str = str + "\n"
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.00001)

def game_won_screen():
    clear_screen()
    print_slow_but_fast("""


                ███████╗            ██╗  ██╗    ██╗   ██╗███████╗ █████╗ ██╗  ██╗
                ██╔════╝▄ ██╗▄▄ ██╗▄██║ ██╔╝    ╚██╗ ██╔╝██╔════╝██╔══██╗██║  ██║
                █████╗   ████╗ ████╗█████╔╝      ╚████╔╝ █████╗  ███████║███████║
                ██╔══╝  ▀╚██╔▀▀╚██╔▀██╔═██╗       ╚██╔╝  ██╔══╝  ██╔══██║██╔══██║
                ██║       ╚═╝   ╚═╝ ██║  ██╗       ██║   ███████╗██║  ██║██║  ██║
                ╚═╝                 ╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                 


    """)

    print_slow_but_fast("""


                ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗    
                ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║    
                 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║    
                  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║    
                   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║    
                   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝    
                                                                


    """)
    time.sleep(0.5)
    
def game_over_screen():
    clear_screen()
    print_slow_but_fast("""

                                    
                ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          



    """)
    print_slow_but_fast("""
    

    
        ██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ███████╗ █████╗ ██████╗     ███╗   ███╗ ██████╗ ████████╗██╗  ██╗███████╗██████╗ ███████╗                  ███████╗██████╗ 
        ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔════╝██╔══██╗██╔══██╗    ████╗ ████║██╔═══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝▄ ██╗▄▄ ██╗▄▄ ██╗▄██╔════╝██╔══██╗
         ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║█████╗  ███████║██║  ██║    ██╔████╔██║██║   ██║   ██║   ███████║█████╗  ██████╔╝█████╗   ████╗ ████╗ ████╗█████╗  ██████╔╝
          ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██╔══╝  ██╔══██║██║  ██║    ██║╚██╔╝██║██║   ██║   ██║   ██╔══██║██╔══╝  ██╔══██╗██╔══╝  ▀╚██╔▀▀╚██╔▀▀╚██╔▀██╔══╝  ██╔══██╗
           ██║   ╚██████╔╝╚██████╔╝    ██████╔╝███████╗██║  ██║██████╔╝    ██║ ╚═╝ ██║╚██████╔╝   ██║   ██║  ██║███████╗██║  ██║██║       ╚═╝   ╚═╝   ╚═╝ ███████╗██║  ██║
           ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝                       ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                  
                                                                                                                                                                  

    """)
    time.sleep(3)


if __name__ == "__main__":
    pass
    #hej2 = validate_int()
    #hej3 = validate_str()
    #print(validate_name())