import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def Sum():
    n = int(I())
    for _ in range(n):
        s = MI()
        O("YES") if sorted(s)[0] + sorted(s)[1] == sorted(s)[2] else O("No")

if __name__ == '__main__':
    Sum()