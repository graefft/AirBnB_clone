#!/usr/bin/python3
"""This module is the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    """Class for command interpreter"""
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        self.close()
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        self.close()
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
        arglist = arg.split()
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
            if key == "BaseModel.{}".format(arglist[1]):
                print(value)
                flag = 1
        if flag == 0:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instances based on the class name and id"""
        if arg == "":
            print("** class name missing **")
            return
        arglist = arg.split()
        try:
            b1 = eval(arglist[0])
        except:
            print("** class doesn't exist **")
            return
        if len(arglist) == 1:
            print("** instance id missing **")
            return
        try:
            dictionary = storage.all()
            for key, value in dictionary.items():
                if key == "{BaseModel}.{}".format(arglist[1]):
                    del dictionary[key]
                    storage.save()
                    break
        except Exception as e:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """Prints string rep of instances"""
        arglist = arg.split()
        if len(arglist) == 0:
            print(storage.all())
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
        arglist = arg.split()
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
        if len(arglist) == 2:
            print("** attribute name missing **")
            return
        if len(arglist) == 3:
            print("** value missing **")
            return
        objectdict = storage.all()
        for key, value in objectdict.items():
            if key == "{}.{}".format(arglist[0], arglist[1]):
                if isint(arglist[3]) is True:
                    setattr(value, arglist[2], int(arglist[3]))
                elif isfloat(arglist[3]) is True:
                    setattr(value, arglist[2], float(arglist[3]))
                else:
                    setattr(value, arglist[2], arglist[3])
                storage.save()

    def close(self):
        """Close file"""
        if self.file:
            self.file.close()
            self.file = None


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
