def add(x,y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y 


def muitiply(x, y):
    """Muitiply Function"""
    return x * y 

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

print(add(3,2))
