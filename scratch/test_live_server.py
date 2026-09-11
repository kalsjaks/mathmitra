import urllib.request
import json

test_queries = [
    'Find the quadratic polynomial whose zeroes are 2 and -1/3',
    'Find roots of x^2 + 5x + 6 = 0',
    'HCF of 900 and 270',
    'Find distance between (2, 3) and (4, 1)',
    '10th term of AP 2, 7, 12',
    '2x + 3y = 11 and 2x - 4y = -24',
    '2x + 5 = 15',
    'Mensuration - Exercise 10.2, Question 1',
    'Real Numbers - Exercise 1.5, Question 5'
]

for q in test_queries:
    data = json.dumps({'query': q}).encode()
    req = urllib.request.Request('http://127.0.0.1:8000/api/solve', data=data, headers={'Content-Type': 'application/json'})
    res = urllib.request.urlopen(req)
    d = json.loads(res.read().decode())
    print(f"OK: {q[:35]:<35} -> {d['chapter_en']}")
