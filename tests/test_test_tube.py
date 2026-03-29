import pytest
from sciencii import test_tube


def test_test_tube_returns_string():
    result = test_tube(50, "Water")
    assert isinstance(result, str)


def test_test_tube_includes_label():
    result = test_tube(50, "Water")
    assert "Water" in result


def test_test_tube_has_fill_blocks():
    result = test_tube(50, "Water")
    assert "###" in result


def test_test_tube_zero_fill():
    result = test_tube(0, "Empty")
    assert "Empty" in result
    assert isinstance(result, str)


def test_test_tube_full_fill():
    result = test_tube(100, "Full")
    assert "Full" in result
    assert result.count("###") >= 1


def test_test_tube_rejects_fill_above_100():
    with pytest.raises(ValueError):
        test_tube(120, "Overflow")


def test_test_tube_rejects_fill_below_0():
    with pytest.raises(ValueError):
        test_tube(-5, "Bad")


def test_test_tube_rejects_non_numeric_fill():
    with pytest.raises(TypeError):
        test_tube("half", "Bad")
        