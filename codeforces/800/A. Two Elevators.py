import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def TwoElevator():
    a,b,c = MII()
    f = a - 1
    if b >=c:
        s = b-1
    else:
        s = b-1
        s += (c-b) * 2
    if f > s:
        return 2
    elif f < s:
        return 1
    else:
        return 3


if __name__ == '__main__':
    for _ in range(II()):
        O(TwoElevator())