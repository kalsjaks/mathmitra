import sympy as sp
import re

# Test coordinate regex
coords_match = re.findall(r'\(\s*([+\-]?\d+(?:\.\d+)?)\s*,\s*([+\-]?\d+(?:\.\d+)?)\s*\)', "Find distance between (2, 3) and (4, 1)")
print("Coords match:", coords_match)

# Test linear system regex
sys_match = re.findall(r'([+\-]?\s*\d*)\s*([a-zA-Z])\s*([+\-]\s*\d*)\s*([a-zA-Z])\s*=\s*([+\-]?\s*\d+)', "2x + 3y = 11 and 2x - 4y = -24")
print("Sys match:", sys_match)

# Test single linear equation
lin_match = re.search(r'([+\-]?\s*\d*)\s*([a-zA-Z])\s*([+\-]\s*\d+)\s*=\s*([+\-]?\s*\d+)', "2x + 5 = 15")
print("Lin match:", lin_match.groups() if lin_match else None)

# Test AP
ap_text = "Find the 10th term of the AP: 2, 7, 12"
m_ap = re.search(r'(\d+)(?:th|st|nd|rd)?\s+term.*?(-?\d+)\s*,\s*(-?\d+)', ap_text, re.IGNORECASE)
print("AP match:", m_ap.groups() if m_ap else None)
