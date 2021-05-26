from words import prefix, suffix
from pytest import approx
import pytest

def test_prefix():
	assert prefix("", "") == approx("")
	assert prefix("", "correct") == approx("")
	assert prefix("clear", "") == approx("")
	assert prefix("happy", "funny") == approx("")
	assert prefix("cat", "catalog") == approx("cat")
	assert prefix("dogmatic", "dog") == approx("dog")
	assert prefix("jump", "joyous") == approx("j")
	assert prefix("unwise", "ungrateful") == approx("un")
	assert prefix("Disable", "dIstasteful") == approx("dis")

def test_suffix():
	assert suffix("", "") == approx("")
	assert suffix("", "correct") == approx("")
	assert suffix("clear", "") == approx("")
	assert suffix("angelic", "awesome") == approx("")
	assert suffix("found", "profound") == approx("found")
	assert suffix("ditch", "itch") == approx("itch")
	assert suffix("happy", "funny") == approx("y")
	assert suffix("tired", "fatigued") == approx("ed")
	assert suffix("swimming", "FLYING") == approx("ing")


path = "E:/GitHub/2021-cs111-programming-with-functions/w05-testing-functions/checkpoint/test_words.py"
path_does_not_work = "test_words.py"
pytest.main(["-v", "--tb=line", "-rN", path_does_not_work])