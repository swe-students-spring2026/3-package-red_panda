"""Unit tests for the dna_helix function."""

import pytest

from sciencii import dna_helix


# Valid inputs

class TestValidInputs:
    def test_length_zero_returns_empty_string(self):
        assert dna_helix(0) == ""

    def test_length_one_returns_five_lines(self):
        result = dna_helix(1)
        assert len(result.split("\n")) == 5

    def test_single_cycle_content(self):
        result = dna_helix(1)
        lines = result.split("\n")
        assert lines[0] == "O---o"
        assert lines[1] == " O-o"
        assert lines[2] == "  O"
        assert lines[3] == " o-O"
        assert lines[4] == "o---O"


# Invalid inputs

class TestInvalidInputs:
    def test_negative_length_raises_value_error(self):
        with pytest.raises(ValueError):
            dna_helix(-1)

    def test_float_raises_type_error(self):
        with pytest.raises(TypeError):
            dna_helix(2.5)

    def test_string_raises_type_error(self):
        with pytest.raises(TypeError):
            dna_helix("3")

    def test_boolean_raises_type_error(self):
        with pytest.raises(TypeError):
            dna_helix(True)


# Structural checks

class TestStructuralChecks:
    def test_pattern_repeats_across_cycles(self):
        result = dna_helix(2)
        lines = result.split("\n")
        assert lines[0] == lines[5] == "O---o"
        assert lines[2] == lines[7] == "  O"
        assert lines[4] == lines[9] == "o---O"
