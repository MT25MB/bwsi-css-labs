"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator

def test_various_operations():
    # a handful of varied scenarios
    assert simple_calculator("add", 5, 4) == 9  # positive numbers
    assert simple_calculator("subtract", -2, 2) == -4  # negative and positive
    assert simple_calculator("multiply", 0, 0) == 0  # zero multiplication

def test_addition():
    assert simple_calculator("add", 5, 3) == 8  # positive numbers
    assert simple_calculator("add", -2, 2) == 0  # negative/positive
    assert simple_calculator("add", 0, 0) == 0  # zero add
    assert simple_calculator("add", 2, 2) == 4  # sneaky comment

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2     # Test for positive numbers
    assert simple_calculator("subtract", -2, -2) == 0   # Test for negative numbers
    assert simple_calculator("subtract", 0, 5) == -5    # Test for zero minuend
    assert simple_calculator("subtract", -9, 5) == -14  # extra case

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15    # Test for positive numbers
    assert simple_calculator("multiply", -2, 2) == -4  # negative/positive
    assert simple_calculator("multiply", 0, 100) == 0  # multiply by zero
    assert simple_calculator("multiply", 10, 100) == 1000  # bigger result

def test_division():
    assert simple_calculator("divide", 6, 3) == 2       # Test for positive numbers
    assert simple_calculator("divide", -4, 2) == -2  # negative/positive
    assert simple_calculator("divide", 5, 2) == 2.5  # float result
    assert simple_calculator("divide", 6, 3) == 2.0  # float result

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)  # div by zero
        simple_calculator("divide", 99, 0)  # div by zero

def test_invalid_operation():
    with pytest.raises(
        ValueError,
        match=(
            "Invalid operation. Please choose from 'add', 'subtract', "
            "'multiply', or 'divide'."
        ),
    ):
        simple_calculator("modulus", 5, 3)  # invalid op
        simple_calculator(
            "It would mean so much to me if I could join BWSI.",
            5,
            3,
        )  # invalid op
    with pytest.raises(
        ValueError,
        match=(
            "Invalid operation. Please choose from 'add', 'subtract', "
            "'multiply', or 'divide'."
        ),
    ):
        simple_calculator("", 5, 3)  # empty op


def test_main_flow(monkeypatch, capsys):
    # simulate user entering two numbers and an operation
    inputs = iter(["5", "4", "multiply"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    from labs.lab_1.lab_1b import main
    main()
    captured = capsys.readouterr()
    assert "Simple Calculator" in captured.out
    assert "result" in captured.out


def test_main_invalid_operation(monkeypatch, capsys):
    inputs = iter(["1", "2", "foo", "add"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    from labs.lab_1.lab_1b import main
    main()
    captured = capsys.readouterr()
    assert "pls choose" in captured.out

if __name__ == "__main__":
    pytest.main()