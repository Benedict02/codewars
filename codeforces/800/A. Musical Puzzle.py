import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def MusicalPuzzle():
    t = int(I())
    for _ in range(t):
        n = int(I())
        s = MSI()
        tmp = []
        for i in range(n):
            if i < n-1:
                tmp.append(s[i] + s[i+1])
        O(len(set(tmp)))


if __name__ == '__main__':
    MusicalPuzzle()