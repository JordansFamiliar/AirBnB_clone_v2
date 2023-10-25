#!/usr/bin/python3
"""This module defines the User class for the HBNB project."""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """User class representing users with various attributes."""

    __tablename__ = 'users'

    if storage_type == 'db':
        # Define columns for the database
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        # Define relationships with Place and Review
        places = relationship('Place', backref='user',
                             cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                              cascade='all, delete, delete-orphan')
    else:
        # Set default values for non-database attributes
        email = ""
        password = ""
        first_name = ""
        last_name = ""
