# https://codeforces.com/problemset/problem/1283/A

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline.replace('\n', ''))

def MinutesBeforeTheNewYear():
    h, m = MII()
    h *= 60
    O(1440-(h+m))

if __name__ == '__main__':
    for _ in range(int(I())):
        MinutesBeforeTheNewYear()