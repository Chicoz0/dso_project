import pickle
from abc import ABC, abstractmethod

from exceptions.generic_exceptions import NotFoundException


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, "wb"))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, "rb"))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def update(self, key, obj):
        if key in self.__cache:
            self.__cache[key] = obj
            self.__dump()
        else:
            raise NotFoundException(f"Item with key {key} not found.")

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            raise NotFoundException

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            raise NotFoundException

    def get_all(self):
        return self.__cache.values()
