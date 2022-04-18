import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_multi_correctly(self):
        assert self.calc.multiply(self, 3, 5) == 15
    def test_substr_correctrly(self):
        assert self.calc.subtraction(self, 10, 5) == 5
    def test_adding_correctly(self):
        assert self.calc.adding(self, 10, 5) == 15
    def test_division_correctly(self):
        assert self.calc.division(self, 10, 5) == 2.0