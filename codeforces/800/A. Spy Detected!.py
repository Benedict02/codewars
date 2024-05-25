import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline.replace('\n', ''))

def SpyDetected():
    n = int(I())
    s = MII()
    if s.count(list(set(s))[0]) > s.count(list(set(s))[1]):
        O(s.index(list(set(s))[1])+1)
    else:
        O(s.index(list(set(s))[0])+1)


if __name__ == '__main__':
    for _ in range(int(I())):
        SpyDetected()