#!/usr/bin/python3
"""Initialize the storage instance for use in the application."""

from os import getenv

# Determine the storage type based on environment variable
storage_type = getenv('HBNB_TYPE_STORAGE')

# Initialize the appropriate storage instance based on the storage type
if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage instance to ensure it's ready for use
storage.reload()
