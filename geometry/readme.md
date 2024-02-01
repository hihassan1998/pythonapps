# geometry

A Python package providing functions to calculate the area of geometric shapes.

## Functions

### `area_of_circle(radius)`

Calculates the area of a circle.

#### Parameters:

- `radius` (float): Radius of the circle.

#### Returns:

- `float`: Area of the circle.

### `area_of_rectangle(length, breadth)`

Calculates the area of a rectangle.

#### Parameters:

- `length` (float): Length of the rectangle.
- `breadth` (float): Breadth of the rectangle.

#### Returns:

- `float`: Area of the rectangle.

## Example Usage:

```python
# Import the functions from the geometry package
from geometry.circle import area_of_circle
from geometry.rectangle import area_of_rectangle

# Test the functions
radius = 5
circle_area = area_of_circle(radius)
print(f"Area of the circle with radius {radius}: {circle_area}")

length = 4
breadth = 6
rectangle_area = area_of_rectangle(length, breadth)
print(f"Area of the rectangle with length {length} and breadth {breadth}: {rectangle_area}")
