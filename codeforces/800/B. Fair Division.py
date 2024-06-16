import sys

def O(s:str, sep='\n'): sys.stdout.write(s + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def FairDivision():
    if sum(a)%2 == 1:
        return "NO"
    else:
        if a.count(1) == 0 and n%2==1:
            return "NO"
        else:
            return "YES"

if __name__ == '__main__':
    for _ in range(II()):
        n = II()
        a = MII()
        O(FairDivision())