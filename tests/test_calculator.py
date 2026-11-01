
import pytest
from calculator import calculate_average


def test_average_normal_input():
    assert calculate_average([10, 20, 30]) == 20


def test_average_empty_input():
    with pytest.raises(ValueError):
        calculate_average([])
