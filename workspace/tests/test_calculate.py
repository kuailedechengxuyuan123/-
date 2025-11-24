import pytest
from src.math_funcs import calculate


def test_both_positive():
    assert calculate(2, 3) == 5


def test_one_negative_x():
    # x < 0 triggers the second branch: x - y
    assert calculate(-2, 3) == -5


def test_one_negative_y():
    # y < 0 triggers the second branch: x - y
    assert calculate(2, -3) == 5


def test_zero_zero():
    # neither >0 nor <0 -> else branch
    assert calculate(0, 0) == 0


def test_boundary_x_zero_y_positive():
    # x == 0 and y > 0 => first branch false, second branch false -> else
    assert calculate(0, 5) == 0


def test_boundary_x_zero_y_negative():
    # y < 0 triggers second branch
    assert calculate(0, -2) == 2
