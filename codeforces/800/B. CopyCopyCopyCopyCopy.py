import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline.replace('\n', ''))

def Copyx5():
    t = int(I())
    for _ in range(t):
        n = int(I())
        s = MII()
        O(len(set(s)))



if __name__ == '__main__':
    Copyx5()