# Optimized!

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def YesOrYes():
    n = int(I()); [O("YES") if "yes" in I().lower() else O("NO") for _ in range(n)]

if __name__ == '__main__':
    YesOrYes()