#!/usr/bin/python3
"""This module is the entry point of the command interpreter"""
import cmd
import re
import sys
import shlex
from shlex import split
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):

    """Class for command interpreter"""
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """creates and saves new instance of BaseModel. Prints id"""
        if arg == "":
            print("** class name missing **")
            return
        arglist = arg.split()
        try:
            b1 = eval(arglist[0])()
            b1.save()
            print(b1.id)
        except:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """prints the string rep of instance based on class name and id"""
        if arg == "":
            print("** class name missing **")
            return
        arglist = parse(arg)
        try:
            b1 = eval(arglist[0])
        except:
            print("** class doesn't exist **")
            return
        if len(arglist) == 1:
            print("** instance id missing **")
            return
        flag = 0
        for key, value in storage.all().items():
            if key == "{}.{}".format(arglist[0], arglist[1]):
                print(value)
                flag = 1
        if flag == 0:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instances based on the class name and id"""
        if arg == "":
            print("** class name missing **")
            return
        arglist = parse(arg)
        try:
            b1 = eval(arglist[0])
        except:
            print("** class doesn't exist **")
            return
        if len(arglist) == 1:
            print("** instance id missing **")
            return
        flag = 0
        dictionary = storage.all()
        for key, value in dictionary.items():
            if key == "{}.{}".format(arglist[0], arglist[1]):
                del dictionary[key]
                storage.save()
                flag = 1
                break
        if flag == 0:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """Prints string rep of instances"""
        arglist = arg.split()
        if len(arglist) == 0:
            objlist = []
            objectdict = storage.all()
            for key, value in objectdict.items():
                objlist.append(str(value))
            print(objlist)

            return
        try:
            model = eval(arglist[0])
        except:
            print("** class doesn't exist **")
            return
        objlist = []
        objectdict = storage.all()
        for key, value in objectdict.items():
            if arglist[0] in key:
                objlist.append(str(value))
        print(objlist)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        arglist = parse(arg)
        if len(arglist) == 0:
            print("** class name missing **")
            return
        try:
            model = eval(arglist[0])
        except:
            print("** class doesn't exist **")
            return
        if len(arglist) == 1:
            print("** instance id missing **")
            return
        objectdict = storage.all()
        flag = 0
        for key, value in objectdict.items():
            if key == "{}.{}".format(arglist[0], arglist[1]):
                flag = 1
        if flag == 0:
            print("** no instance found **")
            return

        if len(arglist) == 2:
            print("** attribute name missing **")
            return
        if len(arglist) == 3:
            print("** value missing **")
            return
        objectdict = storage.all()
        flag = 0
        argument = []
        for word in arglist[2]:
            argument.append(str(word))
        arg_2 = ''.join(argument)
        for key, value in objectdict.items():
            if key == "{}.{}".format(arglist[0], arglist[1]):
                if isint(arglist[3]) is True:
                    setattr(value, arg_2, int(arglist[3]))
                    flag = 1
                elif isfloat(arglist[3]) is True:
                    setattr(value, arg_2, float(arglist[3]))
                    flag = 1
                else:
                    argument = []
                    for item in arglist[3]:
                        argument.append(str(item))
                    arg_3 = ''.join(argument)
                    setattr(value, arg_2, arg_3)
                    flag = 1
                storage.save()

    def close(self):
        """Close file"""
        if self.file:
            self.file.close()
            self.file = None

    def default(self, line):
        '''Override syntax error message '''
        arg_dict = {
                "all": self.do_all,
                "create": self.do_create,
                "destroy": self.do_destroy,
                "show": self.do_show,
                "update": self.do_update
        }
        dot = re.search(r"\.", line)
        if dot:
            cl_comm = [line[:dot.span()[0]], line[dot.span()[1]:]]
            par = re.search(r"\((.*?)\)", cl_comm[1])
            if par:
                command = [cl_comm[1][:par.span()[0]], par.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(cl_comm[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(line))
        return False

    def emptyline(self):
        """Handles empty line"""
        pass

    def preloop(self):
        pass

    def postloop(self):
        '''Adds newline'''
        pass


def parse(arg):
    '''Parses commands for interpreter'''
    return shlex.split(arg)


def isint(string):
    """Test if string content is an int"""
    try:
        int(string)
        return True
    except:
        return False


def isfloat(string):
    """Test if string content is a float"""
    try:
        float(string)
        return True
    except:
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
