from datetime import datetime
from models.event.age_rating import AgeRating
from models.event.attraction import Attraction
from models.location.location import Location
from models.event.tag import Tag


class Event:
    def __init__(
        self,
        name: str,
        date: datetime,
        description: str,
        age_rating: AgeRating,
        location: Location,
    ):
        if not isinstance(name, str) or not name:
            raise Exception("Invalid name")
        if not isinstance(date, datetime) or not date:
            raise Exception("Invalid date")
        if not isinstance(description, str) or not description:
            raise Exception("Invalid description")
        if not isinstance(age_rating, AgeRating) or not age_rating:
            raise Exception("Invalid age rating")
        if not isinstance(location, Location) or not location:
            raise Exception("Invalid location")

        self.__name = name
        self.__date = date
        self.__description = description
        self.__age_rating = age_rating
        self.__location = location
        self.__tags = []
        self.__attractions = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not new_name:
            raise Exception("Invalid name")
        self.__name = new_name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if not isinstance(new_description, str) or not new_description:
            raise Exception("Invalid description")
        self.__description = new_description

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        if not isinstance(new_date, datetime) or not new_date:
            raise Exception("Invalid date")
        self.__date = new_date

    @property
    def age_rating(self):
        return self.__age_rating

    @age_rating.setter
    def age_rating(self, new_age_rating: AgeRating):
        if not isinstance(new_age_rating, AgeRating):
            raise Exception("Invalid age_rating")
        self.__age_rating = new_age_rating

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location: Location):
        if not isinstance(new_location, Location):
            raise Exception("Invalid location")
        self.__location = new_location

    @property
    def tags(self):
        return self.__tags

    def add_tag(self, tag: Tag):
        if not isinstance(tag, Tag):
            raise Exception("Invalid tag")

        for t in self.tags:
            if t.slug == tag.slug:
                return

        self.tags.append(tag)

    def remove_tag(self, tag: Tag):
        if not isinstance(tag, Tag):
            return

        for t in self.tags:
            if t.slug == tag.slug:
                self.tags.remove(tag)
                return

    @property
    def attractions(self):
        return self.__attractions

    def add_attraction(self, attraction: Attraction):
        if not isinstance(attraction, Attraction):
            raise Exception("Invalid attraction")

        for a in self.attractions:
            if a.name == attraction.name:
                return

        self.attractions.append(attraction)

    def remove_attraction(self, attraction: Attraction):
        if not isinstance(attraction, Attraction):
            return

        for a in self.attractions:
            if a.name == attraction.name:
                self.attractions.remove(attraction)
                return
