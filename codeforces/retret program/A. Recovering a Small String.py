# https://codeforces.com/problemset/problem/1931/A

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def RecoveringASmallString():
    n = int(I())
    for _ in range(n):
        a = []
        s = int(I())

        if s > 26:
            a.append(26)
        else:
            a.append(s)
        O(a)



if __name__ == '__main__':
    RecoveringASmallString()