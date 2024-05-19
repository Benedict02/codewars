# https://codeforces.com/problemset/problem/1971/B

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline.replace('\n', ''))

def DifferentString():
    s = I()
    s = [*s]

    lg = len(set(s))
    if lg == 1:
        O("NO")
    else:
        O("YES")
        s = [s[-1]]+s[:-1]
        O("".join([*s]))

if __name__ == '__main__':
    t = int(I())
    for _ in range(t):
        DifferentString()