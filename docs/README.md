# Math formulas

A library for calculation geometric properties of shapes

## Functions description

### Cirсle

- `area` - returns area of circle
- `perimeter` - returns perimeter of circle

```python
from cirсle import area, perimeter

area(1) # 3,14
perimeter(1) # 6,28
```

### Rectangle

- `area` - returns area of rectangle
- `perimeter` - returns perimeter of rectangle

```python
from rectangle import area, perimeter

area(1, 1) # 1
perimeter(1, 2) # 6
```

### Square

- `area` - returns area of square
- `perimeter` - returns perimeter of square

```python
from square import area, perimeter

area(1) # 1
perimeter(1) # 4
```

### Triangle

- `area` - returns area of triangle
- `perimeter` - returns perimeter of triangle

```python
from triangle import area, perimeter

area(1, 1) # 0,5
perimeter(1, 1, 1) # 3
```

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Project modification history

### Commit hash "feeef36"

    - Fixed rectangle.py
    - Added trinagle.py

### Commit hash "f192a86"

    - Added rectangle.py

### Commit hash "d078c8d"


    - Added docs

### Commit hash "8ba9aeb"
   
    - Added circle.py
    - Added rectangle.py

### Commit hash "3102549"
    
    - Tests added

    