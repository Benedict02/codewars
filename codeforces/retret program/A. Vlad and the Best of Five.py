# https://codeforces.com/problemset/problem/1926/A

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def VladAndTheBestOfFive():
    n = int(I())
    for _ in range(n):
        s = list(I())
        O("B") if s.count("A") < s.count("B") else O("A")




if __name__ == '__main__':
    VladAndTheBestOfFive()