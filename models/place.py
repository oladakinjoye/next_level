#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class a place.

    Attributes:
        city_id (str): The City id.
	user_id (str): The User id.
	name (str): The Name of the Place.
        description (str): The Description of the Place.
        number_rooms (int): The number of Rooms of the Place.
        number_bathrooms (int): The number of Bathrooms of the Place.
        max_guest (int): The maximum number of Guests of the Place.
        price_by_night (int): The price by night of the Place.
        latitude (float): The latitude of the Place.
        longitude (float): The longitude of the Place.
        amenity_ids (list): A list of Amenity ids.
    """
        city_id = ""
	user_id = ""
    	name = ""
        description = ""
    	number_rooms = 0
    	number_bathrooms = 0
    	max_guest = 0
    	price_by_night = 0
    	latitude = 0.0
    	longitude = 0.0
    	amenity_ids = []
