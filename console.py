#!/usr/bin/python3

"""
HBNB command-line interpreter module.

This module provides a simple command-line interpreter for HBNB.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    A simple command-line interpreter for HBNB command-line interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        Help for quit command
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
