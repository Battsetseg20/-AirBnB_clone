#!/usr/bin/python3
"""
This module contains the class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class inherits from BaseModel.
    Initializing the public class attributes:

    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
