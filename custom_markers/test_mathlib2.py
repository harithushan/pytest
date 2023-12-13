from mathlib import calc_total, calc_multiply
import pytest
import sys

# -------------------------------------------------------------------
#### To run 
# python -m pytest
# py.test 
# pytest
# python -m pytest -v   
# py.test -v

# -------------------------------------------------------------------

#### unit tets for calc_total
def test_calc_total():
    assert calc_total(2,3) == 5
    assert calc_total(12,23) == 35
    assert calc_total(2,7) == 9
    assert calc_total(2,0) == 2
    assert calc_total(0,0) == 0
    

####unit test for calc_multiply
def test_calc_multiply():
    assert calc_multiply(2,3) == 6
    assert calc_multiply(12,2) == 24
    assert calc_multiply(2,7) == 14
    assert calc_multiply(2,0) == 0
    assert calc_multiply(0,0) == 0
    


    
    