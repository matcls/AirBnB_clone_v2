#!/usr/bin/python3
"""."""

from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import relationship


class DBStorage:
    """Manages databse storage for AirBnB clone"""
    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """List all objects of a given Class"""
        if cls is None:
            self.__objs = self.__session.query(User).all()
            self.__objs.extend(self.__session.query(State).all())
            self.__objs.extend(self.__session.query(City).all())
            self.__objs.extend(self.__session.query(Amenity).all())
            self.__objs.extend(self.__session.query(Place).all())
            self.__objs.extend(self.__session.query(Review).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            self.__objs = self.__session.query(cls)
        dictionary = {"{}.{}".format(obj.__class__.__name__, obj.id):
                      obj for obj in self.__objs}
        return dictionary

    def new(self, obj):
        """Add a new object to database"""
        self.__session.add(obj)

    def save(self):
        """Commit to database"""
        self.__session.commit()

    def delete(self, obj):
        """Deletethe obj from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Initialize the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Removes the session"""
        self.__session.close()
