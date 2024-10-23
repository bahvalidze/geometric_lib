def area(a, h): 
    '''
    Returns area of triangle

    Args:
        a: Side
        h: Height lowered to the side a

    Return:
        float: Triangle's area
    '''
    return float(a * h / 2)

def perimeter(a, b, c): 
    '''
    Returns perimeter of trinagle

    Args:
        a: First side
        b: Secind side
        c: Third side

    Return:
        float: Triangle's perimeter
    '''
    return float(a + b + c)
