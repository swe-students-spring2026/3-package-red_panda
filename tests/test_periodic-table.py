import pytest
from tests.periodic_test_info import names, symbols, fake_symbols, fake_names
from sciencii import get_element
from sciencii.periodic_art import elements
import mendeleev

class Tests:

    #test to make sure all atomic numbers yield an ascii or ineligible numbers don't
    def test_num(self):
        for i in range(1,119):
            element_name = mendeleev.element(i)
            element_name = element_name.name
            expected = elements.get(element_name.lower())
            actual = get_element(i)
            assert actual == expected
        for i in range(-20,1):
            expected = None
            actual = get_element(i)
            assert actual == expected
        for i in range(119, 150):
            expected = None
            actual = get_element(i)
            assert actual == expected


    #test to make sure all symbols work (including fake ones)
    def test_symbol(self):
        for i in range(len(symbols)):
            element_name = mendeleev.element(symbols[i])
            element_name = element_name.name
            expected = elements.get(element_name.lower())
            actual = get_element(symbols[i])
            assert actual == expected
        for i in range(len(fake_symbols)):
            expected = None
            actual = get_element(fake_symbols[i])
            assert actual == expected
    
    #test to make sure all names work (including 'table' and fake names)
    def test_names(self):
        expected = elements.get("table")
        actual = get_element("table")
        assert expected == actual
        for i in range(len(names)):
            element_name = names[i]
            expected = elements.get(element_name.lower())
            actual = get_element(names[i])
            assert actual == expected
        for i in range(len(fake_names)):
            expected = None
            actual = get_element(fake_names[i])
            assert actual == expected


    #test to see if element's name, symbol, and atomic number all yield same result
    def test_name_symbols_num(self):
        for i in range(1,119):
            element_name = mendeleev.element(i)
            element_name = element_name.name
            expected = elements.get(element_name.lower())
            
            actual_name = get_element(names[i-1])
            actual_symbol = get_element(symbols[i-1])
            actual_num = get_element(i)
            assert expected == actual_name == actual_symbol == actual_num

