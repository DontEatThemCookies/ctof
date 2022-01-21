# basic ctof tests (PyTest)
# Run after installing ctof
from ctof import convert


def test_ctof():
    assert convert(32, "C", "F") == 89.6
    assert convert(37.5, "C", "f") == 99.5
    assert convert(30, "c", "K") == 303.15
    assert convert(89.6, "F", "K") == 305.15
    assert convert([400], "k", "f") == 260.33000000000004
    assert convert((42, 100, 38.2), "C", "F") == (107.60000000000001, 212, 100.76)
    assert convert({173.15, 273.15, 373.15}, "K", "C") == {0.0, 100.0, -99.99999999999997}
