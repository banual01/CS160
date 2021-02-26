#!/usr/bin/env python3
"""
`fractions` implementation

@author:
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

        if type(numerator) != int:
            raise TypeError("Numerator must be an integer number")
        elif type(denominator) != int:
            raise TypeError("Denominator must be an integer number")
        else:
            self._numerator = numerator // gcd(numerator,denominator)
            self._denominator = denominator // gcd(numerator,denominator)
            

    def get_numerator(self) -> int:
        """Return fraction numerator"""

        return self._numerator

    numerator = property(get_numerator)

    def get_denominator(self) -> int:
        """Return fraction denominator"""

        return self._denominator

    denominator = property(get_denominator)

    def __str__(self) -> str:
        """Object as a string"""
        if self.numerator > self.denominator:
            mixed_number = self.numerator // self.denominator
            new_numerator = self.numerator - self.denominator * mixed_number        
            return f"{int(mixed_number)} {int(new_numerator)}/{int(self.denominator)}"
        else:
            return str(self._numerator) + "/" + str(self._denominator)

    def __repr__(self) -> str:
        """Object representation"""
        return f"Fraction({str(self._numerator)}, {str(self._denominator)})"


    """using an already establish code in this program, I copypasted it and change the internal function"""

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        if isinstance(other, Fraction):    
            return (
                self.numerator / self.denominator == other.numerator / other.denominator
            )
        raise TypeError("Can only compare Fractions")

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

        if isinstance(other, Fraction):
            if self.denominator == other.denominator:
                total_num = self.numerator + other.numerator
                new_totalnum = total_num // gcd(total_num,self.denominator)
                new_den = self.denominator // gcd(total_num,self.denominator)
                return Fraction(int(new_totalnum), int(new_den))
            else:
                first_num = self.numerator * (other.denominator/gcd(self.denominator, other.denominator))
                second_num = other.numerator * (self.denominator/gcd(self.denominator, other.denominator))
                start_num = first_num + second_num
                start_den = self.denominator * (other.denominator/gcd(self.denominator, other.denominator))
                new_num = start_num // gcd(start_num,start_den)
                new_den =  start_den // gcd(start_num,start_den)
                return Fraction(int(new_num), int(new_den))

        raise TypeError("Can only add two Fractions")


    def __sub__(self, other: object) -> object:
        """Subtract two fractions"""

        """step by step using least common denominator then subtract"""
        """refer back to GCD for simplefied"""

        if isinstance(other, Fraction):
            if self.denominator == other.denominator:
                total_num = self.numerator - other.numerator
                new_totalnum = total_num // gcd(total_num,self.denominator)
                new_den = self.denominator // gcd(total_num,self.denominator)
                return Fraction(int(new_totalnum), int(new_den))
            else:
                first_num = self.numerator * (other.denominator/gcd(self.denominator, other.denominator))
                second_num = other.numerator * (self.denominator/gcd(self.denominator, other.denominator))
                start_num = first_num - second_num
                start_den = self.denominator * (other.denominator/gcd(self.denominator, other.denominator))
                new_num = start_num // gcd(start_num,start_den)
                new_den =  start_den // gcd(start_num,start_den)
                return Fraction(int(new_num), int(new_den))
        raise TypeError("Can only subtract two Fractions")

    def __mul__(self, other: object) -> object:
        """Multiply two fractions"""

        """refer back to GCD for simplefied"""

        if isinstance(other, Fraction):
            total_num = self.numerator * other.numerator
            new_totalnum = total_num // gcd(total_num,self.denominator)
            total_den = self.denominator * other.denominator
            new_totalden = total_den // gcd(total_num,self.denominator)
            return Fraction(int(new_totalnum), int(new_totalden))
        raise TypeError("Can only multiply two Fractions")

    def __truediv__(self, other: object) -> object:
        """Divide two fractions"""
        
        """refer back to GCD for simplefied"""

        if isinstance(other, Fraction):
            total_num = self.numerator * other.denominator
            new_totalnum = total_num // gcd(total_num,self.denominator)
            total_den = self.denominator * other.numerator
            new_totalden = total_den // gcd(total_num,self.denominator)
            return Fraction(int(new_totalnum), int(new_totalden))
        raise TypeError("Can only divide two Fractions")


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
