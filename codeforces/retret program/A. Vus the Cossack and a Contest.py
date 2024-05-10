# https://codeforces.com/problemset/problem/1186/A

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def VusTheCossackAndAContest():
    n, m, k = MI()
    if n <= m and n <= k:
        return "Yes"
    else:
        return "No"




if __name__ == '__main__':
    O(VusTheCossackAndAContest())