#!/usr/bin/python3
"""
Module contains a class HBNBCommand
which is the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models
import json
import shlex

classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """Initializing all attributes and methods:
    prompt: command prompt for Airbnb console
    """
    prompt = '(hbnb)'

    def emptyline(self):
        """ENTER shouldn't execute anything, thus does nothing"""
        pass

    def do_quit(self, *line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *line):
        """Exits the program on Ctrl-d"""
        return True

    def do_create(self, *line):
        """Creates new instance of class"""
        parsed_line = shlex.split(*line)
        if not parsed_line:
            print("** class name missing **")
            return False
        if parsed_line[0] in classes:
            new_instance = classes[parsed_line[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(new_instance.id)
        new_instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
