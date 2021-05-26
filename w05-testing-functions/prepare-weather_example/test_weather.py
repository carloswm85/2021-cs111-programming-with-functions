# test_weather.py

from weather import cels_from_fahr
from pytest import approx
import pytest

def test_cels_from_fahr():
    """Test the cels_from_fahr function by calling it and comparing
    the values it returns to the expected values. Notice this test
    function uses pytest.approx to compare floating point numbers.
    """
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.1111)
    assert cels_from_fahr(-25) == approx(-31.66666)

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
path = 'E:/GitHub/2021-cs111-programming-with-functions/w05-testing-functions/prepare-weather_example/test_weather.py'
pytest.main(["-v", "--tb=line", "-rN", path])