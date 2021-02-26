#!/usr/bin/env python3
"""
Testing the module Touchscreen Keyboard
@authors: Roman Yasinovskyy
@updated: 2019
"""

import time
import pytest

import importlib
import pathlib
import sys

import pytest
sys.path.append('C:\\Users\\alexw\\Desktop\\CS160')

try:
    importlib.util.find_spec("projects.keyboard", "src")
except ModuleNotFoundError:
    sys.path.append(str(pathlib.Path(".").parent.parent.parent.absolute()))
finally:
    from src.projects.keyboard import spell_check

TIME_LIMIT = 4

FILENAMES = (
    "sample",
    "all_firsthalf",
    "all_secondhalf",
    "gen26",
    "gen50",
    "gen100",
    "gen1000",
    "gen2500",
    "gen5000",
    "gen10000",
)

@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename", FILENAMES)
def test_output(filename, capsys):
    """Testing the output"""
    data_in = f"data/projects/keyboard/{filename}.in"
    spell_check(data_in)
    out, err = capsys.readouterr()
    with open(f"tests/projects/keyboard/{filename}.out") as file_out:
        expected_output = file_out.read()
    assert expected_output == out
    assert not err


if __name__ == "__main__":
    pytest.main(["-v", "test_keyboard.py"])
