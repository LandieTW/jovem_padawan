
import pytest

def test_somefunction():
    assert 4 % 2 == 0

@pytest.fixture
def test_otherfunction():
    return lambda n: n ** 2

@pytest.mark.parametrize(("n", "res"), [(2, 4), (6, 37), (13, 169), (-1, 5)])
def test_test_otherfunction(test_otherfunction, n, res):
    assert test_otherfunction(n) == res

@pytest.fixture
def val():
    return 4

@pytest.mark.pair_numbers
def test_pair(val):
    assert val % 2 == 0
