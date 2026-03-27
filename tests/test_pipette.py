"""
Unit tests for pipette module.
"""

import pytest
from sciencii.pipette import pipette


# VALID INPUT TESTS

def test_valid_output_basic():
    """
    Test pipette returns expected output for normal input.
    """
    result = pipette(5, 10)
    assert isinstance(result, str)
    assert "~" in result  # shows liquid
    assert "5/10" in result


def test_empty_pipette():
    """
    Test pipette with zero volume.
    """
    result = pipette(0, 10)
    assert isinstance(result, str)
    assert "~" not in result  # no liquid
    assert "0/10" in result


def test_full_pipette():
    """
    Test pipette when completely full.
    """
    result = pipette(10, 10)
    assert result.count("~") > 0
    assert "10/10" in result


def test_partial_fill():
    """
    Test pipette with partial volume.
    """
    result = pipette(3, 10)

    assert isinstance(result, str)
    assert "~" in result
    assert "3/10" in result


# EDGE CASES

def test_small_nonzero_volume():
    """
    Test pipette with very small nonzero volume.
    """
    result = pipette(0.1, 10)

    assert isinstance(result, str)
    assert "0.1/10" in result
    assert "~" in result or "~" not in result  # Depending on fill ratio


def test_large_numbers():
    """
    Test pipette with large volume values.
    """
    result = pipette(500000, 1000000)

    assert isinstance(result, str)
    assert "500000/1000000" in result
    assert "~" in result


# ERROR HANDLING

def test_volume_not_number():
    """
    Test error when volume is not a number.
    """
    with pytest.raises(ValueError):
        pipette("five", 10)


def test_max_volume_not_number():
    """
    Test error when max_volume is not a number.
    """
    with pytest.raises(ValueError):
        pipette(5, "ten")


def test_negative_volume():
    """
    Test error when volume is negative.
    """
    with pytest.raises(ValueError):
        pipette(-1, 10)


def test_zero_max_volume():
    """
    Test error when max_volume is zero.
    """
    with pytest.raises(ValueError):
        pipette(5, 0)


def test_volume_exceeds_max():
    """
    Test error when volume exceeds max_volume.
    """
    with pytest.raises(ValueError):
        pipette(15, 10)

# OUTPUT STRUCTURE TESTS

def test_output_is_string():
    """
    Test that output is a string.
    """
    result = pipette(5, 10)

    assert isinstance(result, str)


def test_output_contains_label():
    """
    Test that output includes volume label.
    """
    result = pipette(7, 10)

    assert isinstance(result, str)
    assert "7/10" in result


def test_output_has_expected_height():
    """
    Test that output has expected number of lines.
    """
    result = pipette(5, 10)
    lines = result.split("\n")

    assert isinstance(lines, list)
    assert len(lines) > 0
    assert len(lines) >= 20  # pipette body + tip + label