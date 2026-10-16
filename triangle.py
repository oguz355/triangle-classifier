"""Triangle classifier: validates three side lengths and names the triangle type."""
import math


def is_valid_triangle(a, b, c) -> bool:
    """Return True if a, b, c can form a real (non-flat) triangle."""
    # Every side must be a positive length.
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Sort so z is the longest side. Then one check covers the triangle inequality.
    x, y, z = sorted([a, b, c])
    # Strict '>' (not '>=') makes the degenerate case invalid:
    # if x + y == z, the "triangle" is just a flat line.
    return x + y > z


def classify_triangle(a, b, c) -> str:
    """Return "Invalid", or the triangle type with "Right " in front if it has a 90-degree angle."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    # Base type: how many sides are equal?
    if a == b == c:
        kind = "Equilateral"
    elif a == b or b == c or a == c:
        kind = "Isosceles"
    else:
        kind = "Scalene"

    # Right-angle check (Pythagorean theorem) on sorted sides, z = longest.
    x, y, z = sorted([a, b, c])
    # Floats can't store values like sqrt(2) exactly, so compare with a
    # tolerance (math.isclose) instead of ==.
    if math.isclose(x**2 + y**2, z**2):
        return "Right " + kind
    return kind
