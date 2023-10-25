#!/usr/bin/python3
"""State Module for the HBNB project."""
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """State class and table model representing states in the application."""

    # Define the table name for database storage
    __tablename__ = 'states'
    
    # Define attributes for the State class based on the storage type
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """Get a list of City instances with matching state_id.
            
            This method establishes the FileStorage relationship between State and City.
            """
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
