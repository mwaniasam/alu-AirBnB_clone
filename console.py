#!/usr/bin/python3
"""

"""
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB command-line interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
