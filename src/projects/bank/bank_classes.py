#!/usr/bin/env python3
"""
`bank` implementation

@author:
"""

from abc import ABC, abstractmethod


class Address:
    """Address class"""

    def __init__(
        self, street_init: str, city_init: str, state_init: str, zip_init: str
    ):
        """__init__"""
        self._street = street_init
        self._city = city_init
        self._state = state_init
        self._zip = zip_init

    # TODO: Implement data members as properties

    def __eq__(self, other: object):
        """Compare 2 addresses"""
        raise NotImplementedError

    def __str__(self):
        """__str method"""
        raise NotImplementedError


class Customer:
    """Customer class"""

    def __init__(self, name_init: str, dob_init: str, address_init: object):
        """Constructor"""
        self._name = name_init
        self._dob = dob_init
        self._address = Address(address_init)

    # TODO: Implement data members as properties

    def move(self, new_address: object):
        """Change address"""
        raise NotImplementedError

    def __str__(self):
        """__str"""
        raise NotImplementedError


class Account(ABC):
    """Account class"""

    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float = 0):
        """Constructor"""
        self._owner = Customer(owner_init)
        self._balance = balance_init

    # TODO: Implement data members as properties

    def deposit(self, amount: float):
        """Add money"""
        raise NotImplementedError

    def close(self):
        """Close account"""
        raise NotImplementedError

    def __str__(self):
        """__str__"""
        raise NotImplementedError


class CheckingAccount(Account):
    """CheckingAccount class"""

    def __init__(self, owner_init: object, fee_init: float, balance_init: float = 0):
        """Constructor"""
        super().__init__(owner_init, balance_init)
        self._fee = fee_init

    def process_check(self, amount: float):
        """Process a check"""
        raise NotImplementedError

    def __str__(self):
        """__str__"""
        raise NotImplementedError


class SavingsAccount(Account):
    """CheckingAccount class"""

    def __init__(
        self, owner_init: object, interest_rate_init: float, balance_init: float = 0):
        """Constructor"""
        super().__init__(owner_init, balance_init)
        self._interest_rate = interest_rate_init

    def yield_interest(self):
        """Yield annual interest"""
        raise NotImplementedError

    def __str__(self):
        """__str__"""
        raise NotImplementedError
