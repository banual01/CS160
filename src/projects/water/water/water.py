#!/usr/bin/env python3
"""
`water` implementation

@authors: Alexander Banuelos
"""

JUG_1_MAX = 5
JUG_2_MAX = 3


class State:
    """State of the jugs"""

    def __init__(self, jug_1: int, jug_2: int):
        """__init__"""
        if not isinstance(jug_1, int):
            return NotImplemented
        if not isinstance(jug_2, int):
            return NotImplemented
        if jug_1 > JUG_1_MAX:
            raise ValueError(f"The proposed value exceeds jug 1 capacity")
        if jug_2 > JUG_2_MAX:
            raise ValueError(f"The proposed value exceeds jug 2 capacity")
        self.jug_1 = jug_1
        self.jug_2 = jug_2

    def __eq__(self, other: object) -> bool:
        """__eq__"""
        if isinstance(other, State):    
            return (
                self.jug_1 == other.jug_1
                and self.jug_2 == other.jug_2
            )

    def __repr__(self) -> str:
        """__repr__"""
        return f"State({str(self.jug_1)}, {str(self.jug_2)})"

    def __str__(self) -> str:
        """__str__"""
        return f"({self.jug_1}, {self.jug_2})"

    def clone(self):
        """Copy a state"""
        cloneState = State(self.jug_1, self.jug_2)
        return cloneState

    def fill_jug_1(self):
        """Fill jug1 to capacity from the pump"""
        self.jug_1 = JUG_1_MAX

    def fill_jug_2(self):
        """Fill jug2 to capacity from the pump"""
        self.jug_2 = JUG_2_MAX

    def empty_jug_1(self):
        """Pour the water from jug1 onto the ground"""
        self.jug_1 = 0

    def empty_jug_2(self):
        """Pour the water from jug2 onto the ground"""
        self.jug_2 = 0

    def pour_jug_1_to_jug_2(self):
        """Pour as much water as you can from jug1 to jug2 without spilling"""
        if self.jug_1 >= JUG_2_MAX - self.jug_2:
            self.jug_1 -= JUG_2_MAX - self.jug_2
            self.jug_2 += JUG_2_MAX - self.jug_2
        elif self.jug_1 <= self.jug_2:
            self.jug_2 += self.jug_1
            self.jug_1 -= self.jug_1

    def pour_jug_2_to_jug_1(self):
        """Pour as much water as you can from jug2 to jug1 without spilling"""
        if self.jug_2 >= JUG_1_MAX - self.jug_1:
            self.jug_2 -= JUG_1_MAX - self.jug_1
            self.jug_1 += JUG_1_MAX - self.jug_1
        elif self.jug_2 >= self.jug_1:
            self.jug_1 += self.jug_2
            self.jug_2 -= self.jug_2

def search(start_state: State, goal: State, moves_lst: list):
    """Find a sequence of states"""
    newMoves = []
    def checkIn(move):
        if move not in moves_lst:
            newMoves.append(move)
    if start_state not in moves_lst:
        moves_lst.append(start_state)
    if start_state == goal:
        return moves_lst


    for move in moves_lst:
        compareState1 = State.clone(move)
        compareState1.fill_jug_1()
        checkIn(compareState1)

        compareState2 = State.clone(move)         
        compareState2.fill_jug_2()
        checkIn(compareState2)

        compareState3 = State.clone(move)         
        compareState3.empty_jug_1()
        checkIn(compareState3)

        compareState4 = State.clone(move)         
        compareState4.empty_jug_2()
        checkIn(compareState4)

        compareState5 = State.clone(move)         
        compareState5.pour_jug_1_to_jug_2()
        checkIn(compareState5)

        compareState6 = State.clone(move)         
        compareState6.pour_jug_2_to_jug_1()
        checkIn(compareState6)

    uniqueMove = [m for m in newMoves if m not in moves_lst]
    for move in uniqueMove:
        return search(move, goal, moves_lst)