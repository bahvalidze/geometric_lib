import math


def area(r):
    '''
    Returns area of circle

    Args:
        r: Radius

    Return:
        float: Circle's area
    
    Example:
        area(1, 1) # 1
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Returns perimeter of circle

    Args:
        r: Radius

    Return:
        float: Circle's perimeter

    Example:
        perimeter(1, 2) # 6
    '''
    return 2 * math.pi * r

