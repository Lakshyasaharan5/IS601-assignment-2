import operations

def test_add():
    assert operations.add(2, 3) == 5
    assert operations.add(-1, 1) == 0
    assert operations.add(0, 0) == 0

def test_sub():
    assert operations.sub(5, 3) == 2
    assert operations.sub(3, 5) == -2
    assert operations.sub(0, 0) == 0

def test_mul():
    assert operations.mul(4, 2) == 8
    assert operations.mul(-2, 3) == -6
    assert operations.mul(0, 10) == 0

def test_div():
    assert operations.div(10, 2) == 5
    assert operations.div(-9, 3) == -3
    assert operations.div(0, 5) == 0
    assert operations.div(5, 0) == "Error: Division by zero"
