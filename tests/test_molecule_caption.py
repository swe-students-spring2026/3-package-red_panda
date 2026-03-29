import pytest
from sciencii.molecule_caption import molecule_caption, VALID_STYLES


class TestFlaskStyle:
    def test_flask_returns_string(self):
        result = molecule_caption("H2O", "flask")
        assert isinstance(result, str)

    def test_flask_contains_text(self):
        result = molecule_caption("H2O", "flask")
        assert "H2O" in result

    def test_flask_has_neck(self):
        result = molecule_caption("H2O", "flask")
        lines = result.split("\n")
        assert "||" in lines[0]
        assert "||" in lines[1]

    def test_flask_has_base(self):
        result = molecule_caption("H2O", "flask")
        lines = result.split("\n")
        last = lines[-1]
        assert last.startswith("+")
        assert last.endswith("+")
        assert "-" in last

    def test_flask_has_body_with_slashes(self):
        result = molecule_caption("Test", "flask")
        assert "/" in result
        assert "\\" in result


class TestBeakerStyle:
    def test_beaker_returns_string(self):
        result = molecule_caption("NaCl", "beaker")
        assert isinstance(result, str)

    def test_beaker_contains_text(self):
        result = molecule_caption("NaCl", "beaker")
        assert "NaCl" in result

    def test_beaker_has_top_and_bottom_borders(self):
        result = molecule_caption("NaCl", "beaker")
        lines = result.split("\n")
        assert lines[0].startswith("+") and lines[0].endswith("+")
        assert lines[-1].startswith("+") and lines[-1].endswith("+")

    def test_beaker_has_handle(self):
        result = molecule_caption("NaCl", "beaker")
        assert ")" in result

    def test_beaker_has_five_lines(self):
        result = molecule_caption("NaCl", "beaker")
        lines = result.split("\n")
        assert len(lines) == 5


class TestAtomStyle:
    def test_atom_returns_string(self):
        result = molecule_caption("Fe", "atom")
        assert isinstance(result, str)

    def test_atom_contains_text(self):
        result = molecule_caption("Fe", "atom")
        assert "Fe" in result

    def test_atom_has_orbital_brackets(self):
        result = molecule_caption("Fe", "atom")
        assert "({" in result
        assert "})" in result

    def test_atom_has_wave_decoration(self):
        result = molecule_caption("Fe", "atom")
        lines = result.split("\n")
        assert "~" in lines[-1]

    def test_atom_has_four_lines(self):
        result = molecule_caption("Fe", "atom")
        lines = result.split("\n")
        assert len(lines) == 4


class TestBondStyle:
    def test_bond_returns_string(self):
        result = molecule_caption("CO2", "bond")
        assert isinstance(result, str)

    def test_bond_contains_each_character(self):
        result = molecule_caption("CO2", "bond")
        assert "[C]" in result
        assert "[O]" in result
        assert "[2]" in result

    def test_bond_has_connectors(self):
        result = molecule_caption("CO2", "bond")
        assert "-" in result or "=" in result

    def test_bond_single_char(self):
        result = molecule_caption("X", "bond")
        assert result == "[X]"

    def test_bond_alternates_symbols(self):
        result = molecule_caption("ABCD", "bond")
        assert "[A]-[B]=[C]-[D]" == result


# bad inputs should raise errors

class TestInvalidText:
    def test_int_text_raises_type_error(self):
        with pytest.raises(TypeError):
            molecule_caption(123, "flask")

    def test_none_text_raises_type_error(self):
        with pytest.raises(TypeError):
            molecule_caption(None, "flask")

    def test_list_text_raises_type_error(self):
        with pytest.raises(TypeError):
            molecule_caption(["H", "2", "O"], "flask")

    def test_bool_text_raises_type_error(self):
        with pytest.raises(TypeError):
            molecule_caption(True, "flask")

    def test_empty_string_raises_value_error(self):
        with pytest.raises(ValueError):
            molecule_caption("", "flask")


class TestInvalidStyle:
    def test_unknown_style_raises_value_error(self):
        with pytest.raises(ValueError):
            molecule_caption("H2O", "rocket")

    def test_empty_style_raises_value_error(self):
        with pytest.raises(ValueError):
            molecule_caption("H2O", "")

    def test_int_style_raises_type_error(self):
        with pytest.raises(TypeError):
            molecule_caption("H2O", 42)

    def test_none_style_raises_type_error(self):
        with pytest.raises(TypeError):
            molecule_caption("H2O", None)


# edge cases

class TestEdgeCases:
    def test_single_character_all_styles(self):
        for style in VALID_STYLES:
            result = molecule_caption("X", style)
            assert isinstance(result, str)
            assert "X" in result

    def test_long_text(self):
        long = "Deoxyribonucleic Acid"
        result = molecule_caption(long, "beaker")
        assert long in result

    def test_text_with_spaces(self):
        result = molecule_caption("H2 SO4", "atom")
        assert "H2 SO4" in result

    def test_all_valid_styles_accepted(self):
        for style in ("flask", "beaker", "atom", "bond"):
            result = molecule_caption("Test", style)
            assert isinstance(result, str)
            assert len(result) > 0
