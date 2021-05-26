import pytest

# content of test_assert1.py
def f():
    return 3

def test_function():
    assert f() == 3, "It seems to be working."

pytest.main(["-v", "--tb=line", "-rN", "w05-testing-functions/quick_example.py"])