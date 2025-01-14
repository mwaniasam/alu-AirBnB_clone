#!/usr/bin/python3
"""
User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class, contains the users bsic details
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
