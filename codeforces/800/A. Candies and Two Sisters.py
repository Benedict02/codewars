import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def CandiesN2Sisters():
    n = II()
    #I FORGOT PATTERNS AAAAAAA
    return (n-1)//2

if __name__ == '__main__':
    for _ in range(II()):
        O(CandiesN2Sisters())