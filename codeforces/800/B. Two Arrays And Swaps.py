import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def TwoArraysAndSwaps(n, k, a, b):
    a.sort()
    b.sort()
    for i in range(k):
        if a[i] > b[-1]:
            break
        a[i] = b.pop(-1)
    return sum(a)

if __name__ == '__main__':
    for _ in range(II()):
        n, k = MII()
        a = MII()
        b = MII()
        O(TwoArraysAndSwaps(n, k, a, b))