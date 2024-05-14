# Jaka sembung bawa golok, kalo goblok jangan goblok goblok -TH

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def PoliceRecruit():
    n = int(I())
    s = MI()
    p = 0
    e = 0
    for i in range(n):
        if s[i] > 0:
            p += s[i]
        elif s[i] == -1 and p > 0:
            p -= 1
        elif s[i] == -1 and p <= 0:
            e -= 1
    return abs(e)



if __name__ == '__main__':
    O(PoliceRecruit())