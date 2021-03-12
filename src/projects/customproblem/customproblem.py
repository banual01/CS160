#!/usr/bin/env python3
"""
customproblem classes
"""

from abc import ABC, abstractmethod


class Car:
    """Car class"""

    def __init__(self, size_init, speed_init):
        """__init__"""
        self._size = size_init
        self._speed = speed_init


    # TODO: Implement data members as properties

    @property
    def size(self):
        """Get the size"""
        return self._size

    @property
    def speed(self):
        """Get the speed"""
        return self._speed

    def __eq__(self, other: object):
        """Compare 2 Cars"""
        if isinstance(other, Car):    
            return (
                self._size == other._size
                and self._speed == other._speed
            )


    def __str__(self):
        """__str method"""
        return f"{self._}\n{self._}"


class Player:
    """Player class"""

    def __init__(self, name_init, cars_init, inventory_init):
        """Constructor"""
        self._name = name_init
        self._cars = cars_init
        self._inventory = inventory_init



    # TODO: Implement data members as properties

    @property
    def cars(self):
        """Get the cars"""
        return self._cars

    @property
    def name(self):
        """Get the name"""
        return self._name

    @property
    def inventory(self):
        """Get the inventory"""
        return self._inventory

    def __str__(self):
        """__str"""
        return f"{self._}\n{str(self._)}"


class GameMode(ABC):
    """Game Mode class"""

    @abstractmethod
    def __init__(self, player_init, stadium_init, rank_init):
        """Constructor"""
        self._player = player_init
        self._stadium = stadium_init
        self._rank = rank_init


    # TODO: Implement data members as properties

    @property
    def player(self):
        """Get the player"""
        return self._player

    @property
    def stadium(self):
        """Get the stadium"""
        return self._stadium

    @property
    def rank(self):
        """Get the rank"""
        return self._rank

    def __str__(self):
        """__str__"""
        return f"{self._}, {self._}"


class RankMode:
    """Rank Mode class"""

    def __init__(self, drop_init, player_init, stadium_init, rank_init):
        """Constructor"""
        super().__init__(player_init, stadium_init, rank_init)
        self._drop = drop_init


    @property
    def drop_item(self):
        """Get the drop item"""
        return self._drop

    def __str__(self):
        """__str__"""
        return f""


class TournyMode:
    """Tourny Mode class"""

    def __init__(self, credits_init, player_init, stadium_init, rank_init):
        """Constructor"""
        super().__init__(player_init, stadium_init, rank_init)
        self._credits = credits_init


    @property
    def credits(self):
        """Get the credits"""
        return self._credits


    def __str__(self):
        """__str__"""
        return f""
