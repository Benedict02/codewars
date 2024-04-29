# Blindly submitting

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def SquareString():
    n = int(I())
    for _ in range(n):
        s = list(I())
        if len(s) % 2 == 0:
            if "".join(s[int(len(s)/2):]) == "".join(s[:int(len(s)/2)]):
                O("YES")
            else:
                O("NO")
        else:
            O("NO")

if __name__ == '__main__':
    SquareString()