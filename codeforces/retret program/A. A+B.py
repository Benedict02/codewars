# https://codeforces.com/problemset/problem/1772/A

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def APB():
    n = int(I())
    for _ in range(n):
        O(eval(I()))


if __name__ == '__main__':
    APB()