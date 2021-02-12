#!/usr/bin/python3
"""
Module base_model containing the class BaseModel
"""
import uuid
from datetime import datetime
import json


class BaseModel():
    """ Initializing the attributes and methods"""

    def __init__(self):
        """
        Public instance attributes id, created_at and updated_at
        id: string assigned with uuid when an instance is created
        created_at: datetime - assigned when an instance is created
        updated_at: datetime - assigned when instance is created and
        it will be updated every time you change yout object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(tz=None)
        self.updated_at = datetime.now(tz=None)

    def __str__(self):
        """
        Returns string representation of the BaseModel
        format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates  updated_at with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__ of instance
        - By using self.__dict__, only instance attributes set will be returned
        - Add a  key __class__ to this dict with the class name of the object
        - created_at and updated_at coverted to string object in ISO format
        """
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
