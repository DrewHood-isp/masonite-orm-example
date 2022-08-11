# config/database.py
DATABASES = {
  "default": "mysql",
  "mysql": {
    "host": "####",
    "driver": "mysql",
    "database": "masonite",
    "user": "####",
    "password": "####",
    "port": 3306,
    "log_queries": True,
    "options": {
      #
    }
  }
}

from masoniteorm.connections import ConnectionResolver

DB = ConnectionResolver().set_connection_details(DATABASES)
