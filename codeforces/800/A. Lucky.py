
import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def isLucky():
    n = int(I())
    for _ in range(n):
        s = I()
        O("YES" if sum(list(map(int, s[:3]))) == sum(list(map(int, s[3:]))) else "NO")




if __name__ == '__main__':
    isLucky()