#!/usr/bin/python3
"""
Module contains a class HBNBCommand
which is the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Initializing all attributes and methods:
    prompt: command prompt for Airbnb console
    """
    prompt = '(hbnb)'

    def emptyline(self):
        """ENTER shouldn't execute anything, thus returns nothing"""
        pass

    def do_quit(self, *line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *line):
        """Exits the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
