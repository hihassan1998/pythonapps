# Import the function from the geometry module
from geometry.circle import area_of_circle
# Import the function from the rectangle module inside the geometry package
from geometry.rectangle import area_of_rectangle

# Test the function
length = 4
breadth = 6
rectangle_area = area_of_rectangle(length, breadth)
print(f"Area of the rectangle with length {length} and breadth {breadth}: {rectangle_area}")


# Test the function
radius = 5
area = area_of_circle(radius)
print(f"Area of the circle with radius {radius}: {area}")

