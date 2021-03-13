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

    def test_sizespeedratio(self, size, speed):
        """Testing sizespeedratio method"""
        car = Car(self._carname, size, speed)
        car.sizespeedratio(size, speed)
        assert car.ratio == pytest.approx(size / speed, 0.01)
        assert car.strip() == (
            f"{size}:{speed}\n a size-to-speed ratio of {car.ratio}"
        )

    def test_speedbracket(self):
        """Testing speedbracket method"""
        pass

    def test_startinventoryspace(self):
        """Testing startinventoryspace method"""
        pass

    def test_d(self):
        """Testing something"""
        pass

    def test_ranksystem(self):
        """Testing ranksystem method"""
        pass

    def test_prevstadium(self):
        """Testing prevstadium method"""
        pass

    def test_dropsystem(self):
        """Testing dropsystem"""
        pass

    def test_partyrankaver(self):
        """Testing partyrankaver"""
        pass

    def test_tradecredits(self):
        """Testing tradecredits"""
        pass

    def test_creditsgain(self):
        """Testing creditsgain"""
        pass


if __name__ == "__main__":
    pytest.main(["-v", __file__])
