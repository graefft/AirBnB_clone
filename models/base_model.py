#!/usr/bin/python3
"""This module creates the BaseModel class"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A class named BaseModel

    Attributes:
    attr1(id): object id
    attr2(created_at): datetime instance is created
    attr3(updated_at): datetime instance is created and updated when changed
    """
    def __init__(self, *args, **kwargs):
        """Initiliazes an instance"""
        if args is None or kwargs is None:
            return
        if kwargs:
            for key, value in kwargs.items():
                if key is "updated_at" or key is "created_at":
                    datetime_object = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, datetime_object)
                elif key is not "__class__":
                    setattr(self, key, value)    
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns string representation of BaseModel instance"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """updates public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.utcnow()
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        newdict = self.__dict__.copy()
        newdict['created_at'] = datetime.isoformat(newdict['created_at'])
        newdict['updated_at'] = datetime.isoformat(newdict['updated_at'])
        newdict['__class__'] = 'BaseModel'
        return newdict
