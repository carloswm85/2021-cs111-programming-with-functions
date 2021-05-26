from names import make_full_name, extract_given_name, extract_family_name
import pytest

# 1


def test_make_full_name():
	assert make_full_name('Sally', 'Brown') == 'Brown; Sally'
	assert make_full_name('Carlos Washington',
						  'Mercado') == 'Mercado; Carlos Washington'
	assert make_full_name('Lea-Verona', 'Castro') == 'Castro; Lea-Verona'
	assert make_full_name("J", "Ng") == "Ng; J"
	assert make_full_name("", "") == "; "
	
# 2
def test_extract_given_name():
	assert extract_given_name('Brown; Sally') == 'Sally'
	assert extract_given_name('Mercado; Carlos Washington') == 'Carlos Washington'
	assert extract_given_name('Castro; Lea-Verona') == 'Lea-Verona'
	assert extract_given_name("Ng; J") == "J"
	assert extract_given_name("; ") == ""

# 3
def test_extract_family_name():
	assert extract_family_name('Brown; Sally') == 'Brown'
	assert extract_family_name('Mercado; Carlos Washington') == 'Mercado'
	assert extract_family_name('Castro; Lea-Verona') == 'Castro'
	assert extract_family_name("Ng; J") == "Ng"
	assert extract_family_name("; ") == ""

path = 'E:/GitHub/2021-cs111-programming-with-functions/w05-testing-functions/team_activity/test_names.py'
pytest.main(["-v", "--tb=line", "-rN", path])
