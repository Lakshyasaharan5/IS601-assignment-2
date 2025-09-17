def add(x, y):
    """Return the sum of x and y."""
    return x + y

def sub(x, y):
    """Return the difference of x minus y."""
    return x - y

def mul(x, y):
    """Return the product of x and y."""
    return x * y

def div(x, y):
    """Return the division of x by y, or error if y is zero."""
    if y == 0:
        return "Error: Division by zero"
    return x / y
