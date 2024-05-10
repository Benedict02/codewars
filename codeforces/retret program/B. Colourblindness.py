# https://codeforces.com/problemset/problem/1722/B

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

# British
def Colourblindness():
    n = int(I())
    for _ in range(n):
        ns = int(I())
        s1 = I()
        s2 = I()
        s1f = s1.replace('G', 'B')
        s2f = s2.replace('G', 'B')
        O("YES") if s1f == s2f else O("NO")


if __name__ == '__main__':
    Colourblindness()