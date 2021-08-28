import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
        self.shorten_the_fraction()

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        return Fraction(self.top * other.bottom + self.bottom * other.top, self.bottom * other.bottom)

    def shorten_the_fraction(self):
        divisor = math.gcd(self.top, self.bottom)
        self.top //= divisor
        self.bottom //= divisor

