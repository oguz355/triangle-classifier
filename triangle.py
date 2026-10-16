"""Triangle classifier: validates three side lengths and names the triangle type."""
import math


def _is_side_length(value) -> bool:
    """True only for real, finite numbers. Rejects text, blanks, None, True/False, inf, nan."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    return math.isfinite(value)


def is_valid_triangle(a, b, c) -> bool:
    """Return True if a, b, c can form a real (non-flat) triangle."""
    # Bad data (letters, blanks, None) is invalid instead of crashing.
    if not all(_is_side_length(side) for side in (a, b, c)):
        return False
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

    # Pythagorean theorem on sorted sides (z = longest): sqrt(x^2 + y^2) should equal z.
    # math.hypot computes sqrt(x^2 + y^2) without overflowing on huge sides or
    # underflowing on tiny ones, and math.isclose allows for floating-point
    # rounding instead of using ==.
    x, y, z = sorted([a, b, c])
    if math.isclose(math.hypot(x, y), z):
        return "Right " + kind
    return kind