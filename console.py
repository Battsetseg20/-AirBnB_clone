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
    """
    Initializing all attributes and methods:
    prompt: command prompt for Airbnb console
    """
    prompt = '(hbnb) '

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
        """
        Creates new instance of class
        Syntax:create <class>
        """
        parsed_line = shlex.split(*line)
        if not parsed_line:
            print("** class name missing **")
        elif parsed_line[0] in classes:
            new_instance = classes[parsed_line[0]]()
            print(new_instance.id)
            new_instance.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, *line):
        """
        Prints str representation of an instance
        Syntax: show <class name> <id>
        """
        parsed_line = shlex.split(*line)
        if not parsed_line:
            print("** class name missing **")
        elif parsed_line[0] not in classes:
            print("** class doesn't exist **")
        elif len(parsed_line) == 1:
            print("** instance id missing **")
        else:
            name_id = parsed_line[0] + "." + parsed_line[1]
            if name_id in models.storage.all():
                print(models.storage.all()[name_id])
            else:
                print("** no instance found **")

    def do_destroy(self, *line):
        """
        Deletes and instance:
        Syntax: destroy <class> <id>
        Saves the change into the JSON file
        """
        parsed_line = shlex.split(*line)
        if not parsed_line:
            print("**class name missing **")
        elif parsed_line[0] not in classes:
            print("** class doesn't exist **")
        elif len(parsed_line) == 1:
            print("** instance id missing **")
        else:
            name_id = parsed_line[0] + "." + parsed_line[1]
            if name_id in models.storage.all():
                del models.storage.all()[name_id]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, *line):
        """
        Prints all str representation of all instances based
        on OR not on the class name.
        Syntax: all <class> OR all
        """
        parsed_line = shlex.split(*line)
        if not parsed_line:
            for value in models.storage.all().values():
                print(value)
        elif parsed_line[0] in classes:
            for key, value in models.storage.all().items():
                if parsed_line[0] in key:
                    print(value)
        else:
            print("** class doesn't exist **")

    def do_update(self, *line):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        Syntax: update <class name> <id> <attribute name> "<attribute value>"
        Saves the change into JSON file
        """
        parsed_line = shlex.split(*line)
        if len(parsed_line) == 0:
            print("** class name missing **")
        elif parsed_line[0] not in classes:
            print("** class doesn't exist **")
        elif len(parsed_line) == 1:
            print("** instance id missing **")
        elif len(parsed_line) == 2:
            print("** attribute name missing **")
        elif len(parsed_line) == 3:
            print("** value missing **")
        else:
            name_id = parsed_line[0] + "." + parsed_line[1]
            obj = models.storage.all()[name_id]
            name_attrib = parsed_line[2]
            value_attrib = parsed_line[3]
            setattr(obj, name_attrib, value_attrib)
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
