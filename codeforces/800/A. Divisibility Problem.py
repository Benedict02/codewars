import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def Divisibility():
    n = int(I())
    for _ in range(n):
        a, b = MI()
        O((b - a % b)%b)

if __name__ == '__main__':
    Divisibility()