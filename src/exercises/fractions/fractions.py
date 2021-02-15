#!/usr/bin/env python3
"""
Implementation of the class Fraction
"""


def gcd(num_a: int, num_b: int) -> int:
    """
    Greatest Common Denominator of two integers

    Helper function to simplify fractions
    """
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


class Fraction:
    """Class Fraction"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initializer"""
        """if/else function for me to see how programs should go, could be simplefied to for or while function"""
        """this whole thing can be changed"""

        if type(numerator) and type(denominator) != int:
            raise TypeError
        else:
            self._numerator = numerator
            self._denominator = denominator            


    def get_numerator(self) -> int:
        """Return fraction numerator"""

        simple_numerator = self._numerator // gcd(self._numerator,self._denominator)
        
        if simple_numerator > self.denominator:
            mixed_fraction = simple_numerator // gcd(self._numerator,self._denominator)
            simple_numerator -= gcd(self._numerator,self._denominator)

            return f"{mixed_fraction} {simple_numerator - mixed_fraction}"
        else:
            return simple_numerator

    numerator = property(get_numerator)

    def get_denominator(self) -> int:
        """Return fraction denominator"""

        simple_denominator = self._denominator // gcd(self._numerator,self._denominator)

        return simple_denominator

    denominator = property(get_denominator)

    def __str__(self) -> str:
        """Object as a string""" 
        return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self) -> str:
        """Object representation"""
        return f'Fraction(numerator = {str(numerator)}, denominator = {str(denominator)})'

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        if isinstance(other, Fraction):    
            return (
                self.numerator / self.denominator == other.numerator / other.denominator
            )
        raise TypeError("Can only compare Fractions weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

    def __gt__(self, other: object) -> bool:
        """Greater than comparison"""
        if isinstance(other, Fraction):    
            return (
                self.numerator / self.denominator > other.numerator / other.denominator
            )
        raise TypeError("Can only compare Fractions")

    def __ge__(self, other: object) -> bool:
        """Greater than or equal comparison"""
        if isinstance(other, Fraction):
            return (
                self.numerator / self.denominator >= other.numerator / other.denominator
            )
        raise TypeError("Can only compare Fractions")

    def __add__(self, other: object) -> object:
        """Add two fractions"""

        """step by step using least common denominator then adding"""
        """refer back to GCD for simplefied"""

        new_LCDnum = self.numerator + other.numerator
        new_LCDden = self.denominator + other.denominator
        print(gcd(self.denominator, other.denominator))

        return f"{new_LCDnum}/{new_LCDden}"

    def __sub__(self, other: object) -> object:
        """Subtract two fractions"""

        """step by step using least common denominator then subtract"""
        """refer back to GCD for simplefied"""

        return self.numerator / self.denominator - other.numerator / other.denominator

    def __mul__(self, other: object) -> object:
        """Multiply two fractions"""

        """step by step using least common denominator then multiply"""
        """refer back to GCD for simplefied"""

        return self.numerator / self.denominator * other.numerator / other.denominator

    def __truediv__(self, other: object) -> object:
        """Divide two fractions"""

        """step by step using least common denominator then divide"""
        """refer back to GCD for simplefied"""

        return self.numerator / self.denominator / other.numerator / other.denominator


def main():
    """Main function"""
    print("Working with Classes")
    fraction1 = Fraction(10, 4)
    print(f"Fraction 1 is {fraction1}")
    fraction2 = Fraction(10, 12)
    print(f"Fraction 2 is {fraction2}")
    fraction3 = Fraction(3, 4)
    print(f"Fraction 3 is {fraction3}")
    print(f"Its id is {id(fraction3)}")
    fraction4 = Fraction(3, 4)
    print(f"Fraction 4 is {fraction4}")
    print(f"Its id is {id(fraction4)}")

    print("Comparison")
    if fraction3 == fraction4:
        print(f"{fraction3} and {fraction4} are equal!")
    else:
        print(f"{fraction3} and {fraction4} are different!")

    print(f"{fraction1} + {fraction2} = {fraction1 + fraction2}")


if __name__ == "__main__":
    main()
