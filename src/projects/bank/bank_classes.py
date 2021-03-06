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

    @property
    def street(self):
        """Get the street"""
        return self._street

    @property
    def city(self):
        """Get the city"""
        return self._city

    @property
    def state(self):
        """Get the state"""
        return self._state

    @property
    def zip(self):
        """Get the zip"""
        return self._zip


    def __eq__(self, other: object):
        """Compare 2 addresses"""
        try:
            self._street == other._street
            self._city == other._city
            self._state == other._state
            self._zip == other._zip
            return self.address and other.address
        except:
            self._street != other._street
            self._city != other._city
            self._state != other._state
            self._zip != other._zip
            return None

    def __str__(self):
        """__str method"""
        return f"{self._street}\n{self._city}, {self._state} {self._zip}"


class Customer:
    """Customer class"""

    def __init__(self, name_init: str, dob_init: str, address_init: object):
        """Constructor"""
        self._name = name_init
        self._dob = dob_init
        self._address = address_init

    # TODO: Implement data members as properties

    @property
    def name(self):
        """Get the name"""
        return self._name

    @property
    def dob(self):
        """Get the dob"""
        return self._dob

    @property
    def address(self):
        """Get the address"""
        return self._address


    def move(self, new_address: object):
        """Change address"""
        new_address = Address(self._address)
        return new_address

    def __str__(self):
        """__str"""
        return f"{self._name} ({self._dob})\n{str(self._address)}"


class Account(ABC):
    """Account class"""

    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float = 0):
        """Constructor"""
        self._owner = owner_init
        self._balance = balance_init

    # TODO: Implement data members as properties

    @property
    def owner(self):
        """Get the owner"""
        return self._owner

    @property
    def balance(self):
        """Get the balance"""
        return self._balance


    def deposit(self, amount: float):
        """Add money"""
        if amount >= 0:
            self._balance += amount
        else:
            raise ValueError("Must deposit positive amount")

    def close(self):
        """Close account"""
        self._balance = 0
        return round(self._balance, 2)

    def __str__(self):
        """__str__"""
        return f"{self._owner}, {self._balance}"


class CheckingAccount(Account):
    """CheckingAccount class"""

    def __init__(self, owner_init: object, fee_init: float, balance_init: float = 0):
        """Constructor"""
        super().__init__(owner_init, balance_init)
        self._fee = fee_init

    def process_check(self, amount: float):
        """Process a check"""
        if self._balance >= amount:
            new_checamount = self._balance - amount
            return round(new_checamount, 2)
        else:
            new_feeamount = self._balance - self._fee
            return round(new_feeamount, 2)

    def __str__(self):
        """__str__"""
        return f"Checking account\nOwner: {self._owner}\nBalance: {self._balance:.2f}"


class SavingsAccount(Account):
    """CheckingAccount class"""

    def __init__(
        self, owner_init: object, interest_rate_init: float, balance_init: float = 0):
        """Constructor"""
        super().__init__(owner_init, balance_init)
        self._interest_rate = interest_rate_init

    def yield_interest(self):
        """Yield annual interest"""
        new_interaccount = self._balance * (1 + self._interest_rate / 100)
        return round(new_interaccount, 2)

    def __str__(self):
        """__str__"""
        return f"Savings account\nOwner: {self._owner}\nBalance: {self._balance:.2f}"
