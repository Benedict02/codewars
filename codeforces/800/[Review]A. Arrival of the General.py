import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def ArrivalOfTheGeneral():
    n = II()
    a = MII()
    amax = max(a)
    amin = min(a)
    if amin == amax: return 0
    for i in range(n):
        if a[-(i+1)] == amax:
            imax = n - (i+1)
        if a[i] == amin:
            imin = i
    res = (imax - 0) + ((n-1)-imin)
    if imin > imax:
        return res
    if imax > imin:
        return res-1



if __name__ == '__main__':
    O(ArrivalOfTheGeneral())