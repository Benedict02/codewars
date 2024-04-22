# I cant think
import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def PoliceRecruit():
    n = int(I())
    s = I()
    return s.count("-1 1")


if __name__ == '__main__':
    O(PoliceRecruit())