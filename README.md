# Triangle Classifier

Takes three side lengths and returns `"Invalid"`, `"Equilateral"`, `"Isosceles"`, or `"Scalene"`, with `"Right "` in front when the triangle has a 90° angle (for example, `"Right Scalene"`).

## How to run the tests

Mac / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v
```

## Equivalence classes and boundaries

| Class | Example input | Expected result |
|---|---|---|
| A side is zero or negative | (0, 4, 5), (-1, 4, 5) | Invalid |
| Triangle inequality fails | (1, 2, 10) | Invalid |
| Degenerate (two sides add up exactly to the third) | (1, 2, 3) | Invalid |
| Non-numeric or missing input | ("abc", 4, 5), (None, 4, 5) | Invalid |
| All sides equal | (3, 3, 3) | Equilateral |
| Exactly two sides equal | (5, 5, 8) | Isosceles |
| All sides different | (4, 5, 6) | Scalene |
| Right triangle, whole-number sides | (3, 4, 5) | Right Scalene |
| Right triangle, non-whole-number side | (5, 5, 5√2) | Right Isosceles |

Boundaries:

- **Side length:** 0 is invalid; any positive length is allowed.
- **Triangle inequality:** when the two shorter sides add up to exactly the longest side, the shape is a flat line, so (1, 2, 3) is Invalid. Just past that boundary, (1.1, 2, 3) is a valid Scalene.
- **Right-angle check:** uses `math.isclose` instead of `==`, because floating-point rounding means (5√2)² comes out as 50.00000000000001, not exactly 50. It compares `math.hypot` of the two shorter sides to the longest side, so very large (1e200) and very small (1e-200) sides don't overflow or underflow.

## Why an equilateral triangle can never be right

Every angle in an equilateral triangle is 60°, so none of them can be the 90° angle a right triangle needs. In side lengths: a² + a² = 2a², which never equals a² for any positive side a.

## Copilot review log

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
|---|---|---|---|
| test_zero_side_is_invalid | Yes | Edited | Copilot only checked `is_valid_triangle`; added a check that `classify_triangle` returns "Invalid", as the spec table requires |
| test_negative_side_is_invalid | Yes | Edited | Same: only checked validity; added the "Invalid" result check |
| test_triangle_inequality_fails | Yes | Edited | Same: only checked validity; added the "Invalid" result check |
| test_degenerate_triangle_is_invalid | Yes | Edited | Same: only checked validity; added the "Invalid" result check |
| test_equilateral | Yes | Edited | Copilot only checked that 3, 3, 3 is valid, so the test would pass even if the type were wrong; added a check for "Equilateral" |
| test_isosceles | Yes | Edited | Same mistake; added a check for "Isosceles" |
| test_scalene | Yes | Edited | Same mistake; added a check for "Scalene" |
| test_right_scalene | Yes | Edited | Never checked the "Right" prefix; added a check for "Right Scalene" |
| test_right_isosceles_non_integer | Yes | Edited | Never checked the "Right" prefix; added a check for "Right Isosceles" using the exact 5 * math.sqrt(2) |

## Acceptance criteria

The customer's request: *"If it's not a valid triangle, show a message, don't crash. Also flag right-angle pieces. It has to be correct every time."*

1. **Bad input never crashes:** for zero or negative sides, sides that fail the triangle inequality (including the flat 1, 2, 3 case), and non-numeric or missing values ("abc", None, blank), `classify_triangle` returns exactly `"Invalid"` and raises no error.
2. **Right-angle pieces are flagged:** a result starts with `"Right "` if and only if the sides satisfy the Pythagorean theorem, including non-integer sides such as 5, 5, 5√2.
3. **Correct every time:** each reference triangle (3, 3, 3), (5, 5, 8), (4, 5, 6), (3, 4, 5), and (5, 5, 5√2) gets its exact expected label in all 6 orderings of its sides, at normal size, very small (×1e-200), and very large (×1e200).

`test_acceptance.py` checks all three criteria in one end-to-end test.

## AI-use disclosure
**GitHub Copilot (VS Code inline suggestions):** drafted the body of every test in `test_triangle.py`. I checked each suggestion against the spec table. All 9 only checked `is_valid_triangle`, so I edited each one to also check `classify_triangle`'s result.

**Claude (Anthropic):** wrote `triangle.py` and `test_acceptance.py`; helped me review Copilot's suggestions and wrote the corrections; assisted putting together this README. Rewrote my acceptance criteria in better wording. 
