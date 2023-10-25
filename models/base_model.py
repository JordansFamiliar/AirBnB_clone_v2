#!/usr/bin/python3
"""Defines a base class for all models in our hbnb clone."""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage_type

Base = declarative_base()

class BaseModel:
    """Base class for all hbnb models.

    Attributes:
        id (sqlalchemy String): The unique identifier for the model.
        created_at (sqlalchemy DateTime): The creation timestamp.
        updated_at (sqlalchemy DateTime): The last update timestamp.
    """

    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new model instance."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
            if storage_type == 'db':
                if 'id' not in kwargs:
                    setattr(self, 'id', str(uuid.uuid4()))
                if 'created_at' not in kwargs:
                    setattr(self, 'created_at', datetime.now())
                if 'updated_at' not in kwargs:
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Return a string representation of the instance."""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current time when the instance is changed."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert the instance into a dictionary format."""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        for key in instance_dict:
            if isinstance(instance_dict[key], datetime):
                instance_dict[key] = instance_dict[key].isoformat()
        if '_sa_instance_state' in instance_dict:
            del instance_dict['_sa_instance_state']
        return instance_dict

    def delete(self):
        """Delete the current instance from storage."""
        from models import storage
        storage.delete(self)
