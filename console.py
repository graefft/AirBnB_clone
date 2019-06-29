#!/usr/bin/python3
"""This module is the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        self.close()
        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
