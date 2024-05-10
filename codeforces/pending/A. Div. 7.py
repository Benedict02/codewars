# https://codeforces.com/problemset/problem/1633/A

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def Div7():
    n = int(I())
    div7list = [i for i in range(10, 1000) if i % 7 == 0]
    return div7list
    for _ in range(n):
        s = int(I())
        if s % 7 == 0:
            O(s)
        else:
            



if __name__ == '__main__':
    O(Div7())