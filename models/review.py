#!/usr/bin/python3
"""This module defines the Review class for the HBNB project."""

from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_type

class Review(BaseModel, Base):
    """Review class for storing review information."""

    # Define the table name in the database
    __tablename__ = 'reviews'

    # Check the storage type to determine how to handle attributes
    if storage_type == 'db':
        # Define 'text' as a column in the database
        text = Column(String(1024), nullable=False)
        # Define 'place_id' as a foreign key column linked to 'places.id'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        # Define 'user_id' as a foreign key column linked to 'users.id'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        # If not using a database, set 'place_id' and 'user_id' as empty strings
        place_id = ""
        user_id = ""
        text = ""
