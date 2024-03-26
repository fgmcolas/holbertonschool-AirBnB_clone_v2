#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import os

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if  storage_type == 'db':
        reviews = relationship("Review", back_populates="place", cascade="all",
                               passive_deletes=True)
    else:
        @property
        def reviews(self):
            """Return the list of review instances with state.id equal to
            current State.id for filestorage
            """
            from models import storage
            from models.review import Review

            review_list = []
            all_review = storage.all(Review)

            for review in all_review.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
