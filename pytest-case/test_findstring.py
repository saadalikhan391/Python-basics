#You can use a package libraries such as Pytest when automation becomes a priority. Pytest only requires writing functions while a unit test requires classes. This means that pytest has the advantage of being easier because it requires less effort
# from curses.ascii import isdigit
import findstring
import pytest

def test_ispresent():
    assert findstring.ispresent("AL")

# def test_nodigit():
#     assert findstring.nodigit("N7")
    
#python -m pytest test_findstring.py