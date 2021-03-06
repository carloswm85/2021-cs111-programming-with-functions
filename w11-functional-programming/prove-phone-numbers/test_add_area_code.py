# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

from add_area_code import add_area_code
import pytest

def test_add_area_code():
    assert add_area_code("801-412-3210") == "801-412-3210"
    assert add_area_code("656-4771") == "208-656-4771"

path = "E:/GitHub/2021-cs111-programming-with-functions/w11-functional-programming/prove-phone-numbers/test_add_area_code.py"
pytest.main(["-v", "--tb=line", "-rN", path])
