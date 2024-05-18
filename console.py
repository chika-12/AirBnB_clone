#!/usr/bin/python3
"""A console application"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """The console"""

    prompt = '(hbnb) '

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

    def do_EOF(self, arg):
        """Exits the program when EOF is reached"""

        return True

    def emptyline(self):
        """Do nothing to empty line"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
