import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def FairDivision():
    i = MII()
    n = i[0]
    k = i[1]
    l = i[2]
    c = i[3]
    d = i[4]
    p = i[5]
    nl = i[6]
10 1000 1000 25 23 1 50 1    return min(k * l // n // nl, c * d // n, p // n // np)




if __name__ == '__main__':
    O(FairDivision())