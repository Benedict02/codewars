import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline.replace('\n', ''))

def Presents():
    n = int(I())
    s = MII()
    b = []
    for i in range(1, len(s)+1):
        b.append(s.index(i)+1)
    O(str(b).replace("[", "").replace("]", "").replace(",", ""))

if __name__ == '__main__':
    Presents()