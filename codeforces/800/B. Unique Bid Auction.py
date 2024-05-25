# https://codeforces.com/problemset/problem/1454/B/
# -- confused + go learn more about dictionary

import sys
from collections import defaultdict

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def UniqueBidAuction():
    n = II()
    s = MII()
    h = defaultdict(int)
    res = 10**18
    for i in s:
        h[i] += 1
    for j in h:
        if h[j] == 1:
            res = min(j, res)
    if res == 10**18:
        O(-1)
    else:
        O(s.index(res)+1)

if __name__ == '__main__':
    for _ in range(II()):
        UniqueBidAuction()