#!/usr/bin/python3
"""
Module base_model containing the class BaseModel
"""
import uuid
from datetime import datetime
import json
import models


class BaseModel():
    """ Initializing the attributes and methods"""

    def __init__(self, *args, **kwargs):
        """
        *args won't be used

        if **kwargs is not empty:
        - each key of this dictionary is an attribute name
        - each value of this dictionary is the value of this attribute name

        Otherwise: id and created_at assigned when instance is created
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key != '__class__':
                        self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of the BaseModel
        format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates  updated_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__ of instance
        - By using self.__dict__, only instance attributes set will be returned
        - Add a  key __class__ to this dict with the class name of the object
        - created_at and updated_at coverted to string object in ISO format
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
