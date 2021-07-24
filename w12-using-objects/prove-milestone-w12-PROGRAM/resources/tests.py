from classes import fahrenheit_to_celsius
from pytest import approx
import pytest


def test_farenheits_to_celcius():
    farenheit = 23.0
    expected_celcius = -5.00
    result = fahrenheit_to_celsius(farenheit)
    assert result == approx(expected_celcius)


path = 'E:/GitHub/2021-cs111-programming-with-functions/w12-using-objects/prove-milestone-w12-PROGRAM/resources/tests.py'

pytest.main(["-v", "--tb=line", "-rN", path])
