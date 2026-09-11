import sympy as sp
import re

def test_algebra_solver(q):
    print(f"Testing: {q}")
    # Check if linear or quadratic equation
    if '=' in q:
        parts = q.split('=')
        lhs_str = parts[0].strip()
        rhs_str = parts[1].strip()
        print(f"  LHS: {lhs_str}, RHS: {rhs_str}")

test_algebra_solver("2x + 5 = 15")
test_algebra_solver("x^2 - 3x - 10 = 0")
