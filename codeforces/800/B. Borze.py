import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def Borze():
    s = SI()
    s = s.replace('--', '2')
    s = s.replace('-.', '1')
    s = s.replace('.', '0')
    return s

if __name__ == '__main__':
    O(Borze())