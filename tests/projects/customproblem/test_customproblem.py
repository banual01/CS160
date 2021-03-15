#!/usr/bin/env python3
"""
Testing customproblem
"""

import importlib
import pathlib
import sys

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.customproblem import Car, Player, GameMode, RankMode, TournyMode



car_attributes = "carname, size, speed"
cars = [
    ("Octane", "Medium", 52.5),
    ("Merc", "Big", 28.9),
]
player_attributes = "name, cars, inventory"
players = [
    ("John Doe", Car(*cars[0]), 10)
    ("Jane Doe", Car(*cars[1]), 39)
]
gamemode_attributes = "player, stadium, rank"
gamemodes = [
    (Player(*players[0]), "AquaDome", 1000)
    (Player(*players[1]), "Champions Field", 790)
]
rankmode_attributes = "drop, player, stadium, rank"
rankmodes = [
    (35, Player(*players[0]), "AquaDome", 200)
    (45, Player(*players[1]), "DFH Stadium", 850)
]
tournymode_attributes = "credits, player, stadium, rank"
tournymodes = [
    (340058, Player(*players[0]), "Beckwith Park", 1230)
    (8932543, Player(*players[1]), "Neo Tokyo", 397)
]




class TestCustomProblemMethods:
    """Testing module customproblem"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        pass
    

    @pytest.mark.parametrize(car_attributes, cars)
    def test_sizespeedratio(self, size, speed):
        """Testing sizespeedratio method"""
        car = Car(self._carname, size, speed)
        car.sizespeedratio(size, speed)
        assert car.ratio == pytest.approx(size / speed, 0.01)

    # @pytest.mark.parametrize(car_attributes, cars)
    # def test_speedbracket(self):
    #     """Testing speedbracket method"""
    #     car = Car(self._carname, self._size, self._speed)
    #     car.speedbracket(speed)
    #     assert car.speedbracket ==

    @pytest.mark.parametrize(player_attributes, players)
    def test_startinventoryspace(self):
        """Testing startinventoryspace method"""
        assert Car.startinventoryspace == 0

    
    def test_d(self):
        """Testing something"""
        pass
    
    @pytest.mark.parametrize(gamemode_attributes, gamemodes)
    def test_ranksystem(self):
        """Testing ranksystem method"""
        pass

    @pytest.mark.parametrize(gamemode_attributes, gamemodes)
    def test_prevstadium(self):
        """Testing prevstadium method"""
        pass

    @pytest.mark.parametrize(rankmode_attributes, rankmodes)
    def test_dropsystem(self):
        """Testing dropsystem"""
        pass

    @pytest.mark.parametrize(rankmode_attributes, rankmodes)
    def test_partyrankaver(self, other:object, partysize:int):
        """Testing partyrankaver"""
        partysize = 2
        rankmode = RankMode(self._drop, self._player, self._stadium, self._rank)
        rankmode.partyrankaver(partysize) 
        assert rankmodes.rank == pytest.approx(self._rank + other._rank / partysize, 0.01)

    @pytest.mark.parametrize(tournymode_attributes, tournymodes)
    def test_tradecredits(self):
        """Testing tradecredits"""
        creditsbracket = 303453
        tournymodes.tradecredits(creditsbracket)
        assert tournymodes.credits == pytest.approx(
            credits - creditsbracket
            if credits >= creditsbracket
            else
            0.01,
        )
        with pytest.raises(ValueError) as excinfo:
            tournymodes.tradecredits(creditsbracket)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Not enough credits to be traded in for an item"

    @pytest.mark.parametrize(tournymode_attributes, tournymodes)
    def test_creditsgain(self):
        """Testing creditsgain"""
        pass


if __name__ == "__main__":
    pytest.main(["-v", __file__])
