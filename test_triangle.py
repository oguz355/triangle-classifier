import math

from triangle import classify_triangle, is_valid_triangle


def test_zero_side_is_invalid():
    # one side is 0: sides 0, 4, 5
    assert not is_valid_triangle(0, 4, 5)
    assert classify_triangle(0, 4, 5) == "Invalid"


def test_negative_side_is_invalid():
    # one side is negative: sides -1, 4, 5
    assert not is_valid_triangle(-1, 4, 5)
    assert classify_triangle(-1, 4, 5) == "Invalid"


def test_triangle_inequality_fails():
    # two short sides are far too small: sides 1, 2, 10
    assert not is_valid_triangle(1, 2, 10)
    assert classify_triangle(1, 2, 10) == "Invalid"


def test_degenerate_triangle_is_invalid():
    # boundary case: the two short sides add up exactly to the longest: sides 1, 2, 3
    assert not is_valid_triangle(1, 2, 3)
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_equilateral():
    # all sides equal: sides 3, 3, 3
    assert is_valid_triangle(3, 3, 3)
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_isosceles():
    # exactly two sides equal, not a right triangle: sides 5, 5, 8
    assert is_valid_triangle(5, 5, 8)
    assert classify_triangle(5, 5, 8) == "Isosceles"


def test_scalene():
    # all sides different, not a right triangle: sides 4, 5, 6
    assert is_valid_triangle(4, 5, 6)
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_scalene():
    # right triangle with whole-number sides: sides 3, 4, 5
    assert is_valid_triangle(3, 4, 5)
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_isosceles_non_integer():
    # right triangle with a non-integer side: legs 5 and 5, hypotenuse 5 * math.sqrt(2)
    assert is_valid_triangle(5, 5, 5 * math.sqrt(2))
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"