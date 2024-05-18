#!/usr/bin/python3
"""A console application"""

import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The console"""

    prompt = '(hbnb) '

    def __init__(self):
        """Initializes the class"""

        super().__init__()

    def postcmd(self, stop, line):
        """Quit command to exit the program"""

        if line.lower() == 'quit':
            return True
        elif not sys.stdin.isatty():
            return True
        return False

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """Do nothing to empty line"""

        pass

    def do_create(self, args):
        """Creates a BaseModel instance"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
