import addition11
import pytest


def test_add():
    assert addition11.add(4 , 5) == 9

def test_sub():
    assert addition11.sub(4 , 5) == -1


#python -m pytest test_addition.py