from src.negate import negate


def test_name():
    def does_this_return_true():
        return True
    out = False
    
    assert negate(does_this_return_true) == out
    
def test_call_function():
    count = 0
    def testfunc():
        nonlocal count
        count += 1
    
    negate(testfunc)

    assert count == 1

def test_output_negated():
    
    def testfunc():
        return True
    
    expected = False
    assert negate(testfunc) == expected

