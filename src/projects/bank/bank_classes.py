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
        self.street = street_init
        self.city = city_init
        self.state = state_init
        self.zip = zip_init

    # TODO: Implement data members as properties

    def __eq__(self, other: object):
        """Compare 2 addresses"""
        try:
            self.address == other.address
        except:
            self.address is not other.address

    def __str__(self):
        """__str method"""
        return f"{self.street}\n{self.city}, {self.state} {self.zip}"


class Customer:
    """Customer class"""

    def __init__(self, name_init: str, dob_init: str, address_init: object):
        """Constructor"""
        self.name = name_init
        self.dob = dob_init
        self.address = address_init

    # TODO: Implement data members as properties

    def move(self, new_address: object):
        """Change address"""
        raise NotImplementedError

    def __str__(self):
        """__str"""
        return f"{self.name} ({self.dob})\n{str(self.address)}"


class Account(ABC):
    """Account class"""

    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float = 0):
        """Constructor"""
        self.owner = owner_init
        self.balance = balance_init

    # TODO: Implement data members as properties

    def deposit(self, amount: float):
        """Add money"""
        if amount >= 0:
            return self.balance + amount
        else:
            raise ValueError("Must deposit positive amount")

    def close(self):
        """Close account"""
        raise NotImplementedError

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
        return Account.deposit(self, amount)

    def __str__(self):
        """__str__"""
        return f"Checking account\nOwner: {self.owner}\nBalance: {self.balance:.2f}"


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
        return f"Savings account\nOwner: {self.owner}\nBalance: {self.balance:.2f}"
