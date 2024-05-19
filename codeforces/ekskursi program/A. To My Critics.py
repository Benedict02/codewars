# https://codeforces.com/problemset/problem/1850/A

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline.replace('\n', ''))

def ToMyCritics():
    s = MII()
    s.sort()
    if s[-1] + s[len(s)-2] >= 10:
        O("YES")
    else:
        O("NO")

if __name__ == '__main__':
    for _ in range(int(I())):
        ToMyCritics()