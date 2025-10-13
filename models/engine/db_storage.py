#!/usr/bin/python3
"""Defines the DBStorage engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Manages storage of hbnb models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database connection"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects or objects of a specific class"""
        objects = {}
        classes = {
            "State": State,
            "City": City,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity
        }

        if cls:
            query = self.__session.query(cls).all()
        else:
            query = []
            for clss in classes.values():
                query.extend(self.__session.query(clss).all())

        for obj in query:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects[key] = obj
        return objects

    def new(self, obj):
        """Add object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Remove the current SQLAlchemy session"""
        self.__session.remove()
