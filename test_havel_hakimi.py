import havel_hakimi as hh
import pytest


def test_list_contains_negative_number():
    with pytest.raises(ValueError):
        hh.non_negative_list([-9])
    with pytest.raises(ValueError):
        hh.havel_hakimi([-9])
    with pytest.raises(ValueError):
        hh.non_negative_list([-9.4])


def test_list_contains_non_negative_number():
    hh.non_negative_list([6, 7, 9.5])


def test_list_contains_integers():
    with pytest.raises(ValueError):
        hh.integer_list([6, 7, 9.5])
    with pytest.raises(ValueError):
        hh.havel_hakimi([6, 7, 9.5])
    hh.integer_list([3, 4, 5, 6, 7])


def test_havel_hakimi():
    assert hh.havel_hakimi([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]) is False
    assert hh.havel_hakimi([4, 2, 0, 1, 5, 0]) is False
    assert hh.havel_hakimi([3, 1, 2, 3, 1, 0]) is False
    assert hh.havel_hakimi([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]) is False

