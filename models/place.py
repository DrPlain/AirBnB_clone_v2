#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models import storage_type
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)

    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)

    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)

    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if storage_type == 'db':
        reviews = relationship('Review',
                               backref='place',
                               cascade='all, delete')
    else:
        @property
        def reviews(self):
            """"""
            from models import storage
            revs = storage.all(Review)
            reviews = []
            for rev in revs.values():
                if self.id == rev.place_id:
                    reviews.append(rev)
            return reviews
