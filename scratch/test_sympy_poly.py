import sympy as sp
import re

def parse_equation_or_expr(raw_str):
    # Normalize ^ to **
    s = raw_str.replace('^', '**')
    # Insert * between number and letter, e.g. 2x -> 2*x
    s = re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', s)
    # Insert * between )( -> )*(
    s = re.sub(r'\)\s*\(', r')*(', s)
    print(f"Sanitized '{raw_str}' -> '{s}'")
    try:
        if '=' in s:
            lhs_s, rhs_s = s.split('=', 1)
            lhs = sp.sympify(lhs_s.strip())
            rhs = sp.sympify(rhs_s.strip())
            eq = sp.Eq(lhs, rhs)
            vars = list(eq.free_symbols)
            sols = sp.solve(eq, vars)
            print(f"  Solved Eq {eq}: vars={vars}, sols={sols}")
            return eq, vars, sols
        else:
            expr = sp.sympify(s)
            vars = list(expr.free_symbols)
            roots = sp.solve(expr, vars)
            print(f"  Solved Expr {expr}: vars={vars}, roots={roots}")
            return expr, vars, roots
    except Exception as e:
        print(f"  Failed: {e}")
        return None

parse_equation_or_expr("x^2 - 2x - 8")
parse_equation_or_expr("2x + 5 = 15")
parse_equation_or_expr("x^2 + 5x + 6 = 0")
parse_equation_or_expr("x^2 - 16 = 0")
parse_equation_or_expr("4u^2 + 8u")
parse_equation_or_expr("3x^2 - x - 4")
