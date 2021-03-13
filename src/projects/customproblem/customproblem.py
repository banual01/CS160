#!/usr/bin/env python3
"""
customproblem classes
"""

from abc import ABC, abstractmethod


class Car:
    """Car class"""

    def __init__(self, carname_init, size_init, speed_init):
        """__init__"""
        self._carname = carname_init
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

    @property
    def car_name(self):
        """Get the car's name"""
        return self._carname

    def __eq__(self, other: object):
        """Compare 2 Cars"""
        if isinstance(other, Car):    
            return (
                self._size == other._size
                and self._speed == other._speed
                and self._carname == other._carname
            )

    def sizespeedratio(self, size:float, speed:float):
        ratio = size / speed

    def speedbracket(self):
        if 0 < speed <= 20:
            return "This is a slow car"
        elif speed > 20:
            return "This is a speedy car"


    def __str__(self):
        """__str method"""
        return f"{self._carname}: {self._size}\n Speed: {self._speed}"


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

    def startinventoryspace(self):
        self._inventory = 0

    def __str__(self):
        """__str"""
        return f"{self._name}\n{str(self._cars)}\n{str(self._inventory)}"


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

    # def ranksystem(self, unranked:int, win:dictionary):
    #     for 

    # def prevstadium(self, other:object):
    #     while self._stadium == other._stadium:


    def __str__(self):
        """__str__"""
        return f"{self._player}\nFavorite Stadium:{self._stadium}\nRank:{self._rank}"


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

    # def dropsystem(self, win:dictionary):
    #     for

    def partyrankaver(self, other:object, partysize:int):
        totalparty_rank = self._rank + other._rank
        return totalparty_rank / partysize


    def __str__(self):
        """__str__"""
        return f"{self._player}\nFavorite Stadium:{self._stadium}\nRank:{self._rank}\nDrops:{self._drop}"


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

    def __eq__(self, other:object):
        """Compare 2 players's tourny bracket placement"""
        if isinstance(other, TournyMode):    
            return (
                self._rank == other._rank
            )
        else:
            raise ValueError("Not in the same tourny bracket")

    def tradecredits(self, creditsbracket:int):
        if self._credits >= creditsbracket:
            self._credits = self._credits - creditsbracket
        else:
            raise ValueError("Not enough credits to be traded in for an item")
    
    # def creditsgain(self, addcredits:int, win:dictionary):
    #     for


    def __str__(self):
        """__str__"""
        return f"{self._player}\nFavorite Stadium:{self._stadium}\nRank:{self._rank}\nCredits:{self._credit}"
