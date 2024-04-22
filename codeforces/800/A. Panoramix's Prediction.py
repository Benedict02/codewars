# This problem is rage inducing. Im doing this in midnight & my brain is not in an ideal state
import sys, math

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))


def Panoramix():
    prime = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    n, m = MI()
    if m in prime:
        if prime[prime.index(n) + 1] == m:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

if __name__ == '__main__':
    O(Panoramix())