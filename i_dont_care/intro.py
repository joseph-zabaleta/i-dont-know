# Inpiration gained from research on the pyfiglet library. Inspiration gained from: https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text

import sys
from textwrap import dedent
from colorama import init
init(strip=not sys.stdout.isatty())

from termcolor import cprint 
from pyfiglet import figlet_format as fig

def intro():
    test = fig("""Honey. . . 
       I 
don't 
care
""", font="starwars")
    cprint(test, 'cyan', attrs=['bold'])

intro()
