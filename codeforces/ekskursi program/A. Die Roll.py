# https://codeforces.com/problemset/problem/9/A

import sys
from fractions import Fraction

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline.replace('\n', ''))


def DieRoll():
    x, y = MII()
    m = max(y, x)
    d = 6 - m + 1
    if 6 % d == 0:
        return (f"1/{6//d}")
    elif d == 4:
        return (f"2/3")
    else:
        return (f"{d}/6")


if __name__ == '__main__':
    O(DieRoll())