# Will my code TLE?

import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def AntonNPolyhedrons():
    n = int(I())
    res = 0
    for i in range(n):
        s = I()
        if s == "Tetrahedron":
            res += 4
        if s == "Cube":
            res += 6
        if s == "Octahedron":
            res += 8
        if s == "Dodecahedron":
            res += 12
        if s == "Icosahedron":
            res += 20
    return res

if __name__ == '__main__':
    O(AntonNPolyhedrons())