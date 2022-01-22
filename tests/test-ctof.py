# ctof 0.2.0 tests (PyTest)
# Run after installing ctof
import pytest
from   ctof import convert



def test_ctof():
    # Basic functionality tests
    assert convert(32, "C", "F") == 89.6
    assert convert(89.6, "F", "F") == 89.6
    assert convert(37.5, "C", "f") == 99.5
    assert convert(30, "c", "K") == 303.15
    assert convert(89.6, "f", "k") == 305.15
    assert convert([400], "K", "F") == 260.33000000000004
    assert convert((42, 100, 38.2), "C", "F") == (107.60000000000001, 212, 100.76)
    assert convert({173.15, 273.15, 373.15}, "K", "C") == {0.0, 100.0, -99.99999999999997}

    # Exception tests
    with pytest.raises(TypeError) as exc:
        convert("thirty-two", "C", "F")
        assert str(exc.value) == "parameter 'values' not of type int/float/list/tuple/set"
    with pytest.raises(TypeError) as exc:
        convert(32, "C", b"F")
        assert str(exc.value) == "_from and _to arguments must be a string"
    with pytest.raises(ValueError) as exc:
        convert(89.6, "Fahrenheit", "C")
        assert str(exc.value) == "_from and _to arguments must be 'C', 'F' or 'K'"
    with pytest.raises(TypeError) as exc:
        convert(["32", 33, 34], "C", "F")
        assert str(exc.value) == "at least one iterable member is not an int/float"
