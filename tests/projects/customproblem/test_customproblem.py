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
    ("Merc", "Big", 28.9)
]
player_attributes = "name, cars, inventory, won"
players = [
    ("John Doe", Car(*cars[0]), 10, 30),
    ("Jane Doe", Car(*cars[1]), 39, 40)
]
gamemode_attributes = "player, stadium, result"
gamemodes = [
    (Player(*players[0]), "AquaDome", "Win"),
    (Player(*players[1]), "Champions Field", "Lose")
]
rankmode_attributes = "drop, player, stadium, rank"
rankmodes = [
    (35, Player(*players[0]), "AquaDome", "Gold"),
    (45, Player(*players[1]), "DFH Stadium", "Bronze")
]
tournymode_attributes = "credits, player, stadium, rank"
tournymodes = [
    (340058, Player(*players[0]), "Beckwith Park", "Gold"),
    (8932543, Player(*players[1]), "Neo Tokyo", "Silver")
]




class TestCustomProblemMethods:
    """Testing module customproblem"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        pass
    

    @pytest.mark.parametrize(car_attributes, cars)
    def test_sizeSpeedRatio(self, carname, size, speed):
        """Testing sizespeedratio method"""
        car = Car(self._carname, size, speed)
        car.sizespeedratio(carname, size, speed)
        assert car.ratio == pytest.approx(size / speed, 0.01)

    # @pytest.mark.parametrize(car_attributes, cars)
    # def test_speedBracket(self):
    #     """Testing speedBracket method"""
    #     car = Car(self._carname, self._size, self._speed)
    #     car.speedbracket(speed)
    #     assert car.speedbracket ==


    def test_startInventorySpace(self):
        """Testing startinventoryspace method"""
        assert Car.startinventoryspace == 0

    
    def test_gameResult(self):
        """Testing gameresult method"""
        pass


    def test_rankChange(self):
        """Testing ranksystem method"""
        pass


    def test_addItem(self):
        """Testing additem method"""
        pass


    def test_dropSystem(self):
        """Testing dropsystem"""
        pass


    def test_partyRankAver(self, other:object, partysize:int):
        """Testing partyrankaver"""
        partysize = 2
        rankmode = RankMode(self._drop, self._player, self._stadium, self._rank)
        rankmode.partyrankaver(partysize) 
        assert rankmodes.rank == pytest.approx(self._rank + other._rank / partysize, 0.01)


    def test_tradeCredits(self):
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


    def test_dropCredit(self):
        """Testing creditsgain"""
        pass


if __name__ == "__main__":
    pytest.main(["-v", __file__])
