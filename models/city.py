#!/usr/bin/python3
"""
This module contains the class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class inherits from BaseModel.
    Initializing the public class attributes:

    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""
