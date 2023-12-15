#### skiping the test : pytest -v -rsx
@pytest.mark.skip(reason= "I don't want to run this test at the moment")
def test_calc_total_1():
    assert calc_multiply(12,2) == 24
    
#### skiping with a condition
@pytest.mark.skipif(sys.version_info < (3,5), reason= "I don't want to run this test at the moment")
def test_calc_total_2():
    assert calc_multiply(12,2) == 24

#### to run only the test which contains "multiply" in their test name
# pytest -k multiply -v test_skip.py
