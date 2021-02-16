#!/usr/bin/python3
"""
This module contains the class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class inherits from BaseModel.
    Initializing the public class attributes:

    place_id: str - empty string: it will be the Place.id
    user_id: str - empty string: it will be the User.id
    text: str - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
