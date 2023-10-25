#!/usr/bin/python3
"""This module defines the Amenity class for the HBNB project."""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """Amenity class for storing amenity information."""

    # Define the table name in the database
    __tablename__ = 'amenities'

    # Check the storage type to determine how to handle 'name'
    if storage_type == 'db':
        # Define 'name' as a column in the database
        name = Column(String(128), nullable=False)
    else:
        # If not using a database, set 'name' as an empty string
        name = ""
