import pytest
import calculator

calculator = calculator.Calculator()


def test_addition():
    assert calculator.addition(2, 2) == 4


def test_subtraction():
    assert calculator.subtraction(4, 2) == 2


def test_division():
    assert calculator.division(9, 3) == 3


def test_multiplication():
    assert calculator.multiplication(3, 3) == 9


def test_pow():
    assert calculator.pow(2, 4) == 16
