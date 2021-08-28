from main import Calculator

def test_add():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.add() == x + y, "Add method doesn't work"

def test_subtract():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.subtract() == x-y, "Subtract method doesn't work"

def test_divide():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.divide() == x/y, "Divide method doesn't work"

def test_multiply():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.multiply() == x*y, "Multiply method does not work"
