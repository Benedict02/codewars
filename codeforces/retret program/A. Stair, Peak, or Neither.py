# https://codeforces.com/problemset/problem/1950/A

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def StairPeakOrNeither():
    n = int(I())
    for _ in range(n):
        a, b, c = MI()
        if a < b and b < c:
            O("STAIR")
        elif a < b and b > c:
            O("PEAK")
        else:
            O("NONE")



if __name__ == '__main__':
    StairPeakOrNeither()