"""Acceptance test for the stained-glass studio's requirements.

AC1 - Bad input never crashes: for zero or negative sides, sides that fail the
      triangle inequality (including the flat 1, 2, 3 case), and non-numeric or
      missing values ("abc", None, blank), classify_triangle returns exactly
      "Invalid" and raises no error.
AC2 - Right-angle pieces are flagged: a result starts with "Right " if and only
      if the sides satisfy the Pythagorean theorem, including non-integer sides
      such as 5, 5, 5 * sqrt(2).
AC3 - Correct every time: each reference triangle gets its exact expected label
      in all 6 orderings of its sides, at normal size, very small (x 1e-200),
      and very large (x 1e200).
"""
import itertools
import math

from triangle import classify_triangle

BAD_INPUTS = [
    (0, 4, 5),          # zero side
    (-3, 4, 5),         # negative side
    (1, 2, 10),         # triangle inequality fails
    (1, 2, 3),          # degenerate: flat line
    ("abc", 4, 5),      # letters
    ("a", "b", "c"),    # all letters
    (None, 4, 5),       # missing value
    ("", "", ""),       # blank boxes
]

REFERENCE_TRIANGLES = [
    ((3, 3, 3), "Equilateral"),
    ((5, 5, 8), "Isosceles"),
    ((4, 5, 6), "Scalene"),
    ((3, 4, 5), "Right Scalene"),
    ((5, 5, 5 * math.sqrt(2)), "Right Isosceles"),
]

SCALES = [1, 1e-200, 1e200]


def test_stained_glass_customer_requirements():
    # AC1: bad input returns "Invalid" (any crash would fail this test)
    for sides in BAD_INPUTS:
        assert classify_triangle(*sides) == "Invalid", f"{sides} should be Invalid"

    # AC2 + AC3: every ordering and size gets the exact expected label
    for sides, expected in REFERENCE_TRIANGLES:
        for scale in SCALES:
            scaled = [side * scale for side in sides]
            for order in itertools.permutations(scaled):
                result = classify_triangle(*order)
                assert result == expected, f"{order} gave {result}, expected {expected}"
                # AC2: "Right " appears only on right-angle pieces
                assert result.startswith("Right ") == expected.startswith("Right ")