# Inpiration gained from research on the pyfiglet library. Inspiration gained from: https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text
# Menu Inspiration Youtube Video Part 1) https://www.youtube.com/watch?v=BK7YvpTT4Sw&list=PLyb_C2HpOQSBxk3yBBcrUHReH9BwMUYhG
# Menu Inspiration Youtube Video Part 2) https://www.youtube.com/watch?v=zwMsmBsC1GM
# Menu Notebooks / Repo for documentation : https://github.com/nikhilkumarsingh/python-curses-tut

# Menu Libraries
import time
import curses 

#ASCII Art Libraries 
from termcolor import cprint 
from pyfiglet import figlet_format as fig

menu = ['Start', 'History(Coming Soon)', 'Random(Coming Soon)', 'Exit']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    
    # text = fig('Honey... I don\'t know', font='starwars')
    # stdscr.addstr(0, 0, text)
    # stdscr.refresh()

    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0) # turns blinker on (1) off (0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # color scheme, (foreground, then background color)
    current_row = 0 # default row to start on
    print_menu(stdscr, current_row) # print the main menu

    status = True

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:

            if current_row == 0:
              stdscr.clear()
              print_center(stdscr, 'Starting app...')
              stdscr.refresh()
              time.sleep(3)
              break
            
            if current_row == 1 or current_row == 2:
                print_center(stdscr, "Sorry! '{}' is still be developed".format(menu[current_row]))
                stdscr.getch()
            
            if current_row == 3: #exit the program
                print_center(stdscr, 'Thanks!')
                time.sleep(3)
                status = False
                break 

        print_menu(stdscr, current_row)
    return status

# result = curses.wrapper(main)

