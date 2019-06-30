#!/usr/bin/python3
"""This module serializes and deserializes instances"""

import json
from models.base_model import BaseModel
from models.user import User
from os import path


class FileStorage:
    """A class named FileStorage
    Attributes:
    attr1(__file_path): path to the JSON file
    attr2(__objects): dictionary for all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as w:
            json.dump(dictionary, w)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dictionaryofdictionaries = {}
        classes = {
                "BaseModel": BaseModel,
                "User": User}
        try:
            with open(self.__file_path, "r") as r:
                dictionaryofdictionaries = json.load(r)
                for key, v in dictionaryofdictionaries.items():
                    if v["__class__"] in classes:
                        self.__objects[key] = classes[v["__class__"]](**v)
        except:
            pass
