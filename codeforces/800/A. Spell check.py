# Im drunk
import sys, collections

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def CheckSpell():
    n = int(I())
    for _ in range(n):
        b = I()
        s, i = collections.Counter("Timur"), collections.Counter(I())
        if s == i:
            O("YES")
        else:
            O("NO")

if __name__ == '__main__':
    CheckSpell()