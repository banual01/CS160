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
    ("Octane", 34, 52.5),
    ("Merc", 272, 28.9)
]
player_attributes = "name, cars, inventory, won"
players = [
    ("John Doe", Car(*cars[0]), {"Tournament": 0, "Ranking": []}, 30),
    ("Jane Doe", Car(*cars[1]), {"Tournament": 0, "Ranking": []}, 40)
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
    (3058, Player(*players[0]), "Beckwith Park", "Gold"),
    (8932543, Player(*players[1]), "Neo Tokyo", "Silver")
]



class TestCustomProblemMethods:
    """Testing module customproblem"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        


    def test_sizeSpeedRatio(self, size, speed):
        """Testing sizespeedratio method"""
        assert Car.ratio == pytest.approx(size/speed, 0.01)

    # @pytest.mark.parametrize(car_attributes, cars)
    # def test_speedBracket(self):
    #     """Testing speedBracket method"""
    #     assert car.speedbracket ==


    def test_startInventorySpace(self):
        """Testing startinventoryspace method"""
        assert Player.startInventorySpace == {"Tournament": 0, "Ranking": []}

    
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
        assert rankmodes.rank == pytest.approx(self._rank + other._rank / partysize, 0.01)


    def test_tradeCredits(self):
        """Testing tradecredits"""
        creditsbracket = 303453
        tournymodes.tradeCredits(creditsbracket)
        assert tournymodes.credits == pytest.approx(
            credits - creditsbracket
            if credits >= creditsbracket
            else
            0.01,
        )
        with pytest.raises(ValueError) as excinfo:
            tournymodes.tradeCredits(creditsbracket)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Not enough credits to be traded in for an item"


    def test_dropCredit(self):
        """Testing creditsgain"""
        pass


if __name__ == "__main__":
    pytest.main(["-v", __file__])
