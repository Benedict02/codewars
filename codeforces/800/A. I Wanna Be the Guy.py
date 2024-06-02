import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def FuncName():
    n = II()
    p = MII()
    q = MII()
    if len(list(set(p[1:]+q[1:]))):
        return "I become the guy."
    else:
        return "Oh, my keyboard!"



if __name__ == '__main__':
    O(FuncName())