import pytest
from source.my_functions import *
import time

def test_add_numbers():
    assert add(2,3) == 5
    assert add(2,2) == 4
    
def test_divide_numbers():
    assert divide(10, 2)== 5
    assert divide(10, 2)== 5.0
        
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
        
def test_add_strings():
    assert add("hello", "world") == "helloworld"
    assert add("hello", " ") == "hello "
    
## mark : slow    run using ----->  pytest -m slow

@pytest.mark.slow    
def test_very_slow():
    time.sleep(3)
    result= divide(10, 5)
    time.sleep(2)
    assert result == 2
    
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert add(1, 2) == 3

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    divide(4, 0)