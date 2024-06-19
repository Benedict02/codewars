import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def Nikita(n, m):
    if n >= m and (n-m)%2==0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    for _ in range(II()):
        n, m = MII()
        O(Nikita(n, m))