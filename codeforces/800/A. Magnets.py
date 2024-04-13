import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')

def Magnets():
    n = int(I())

if __name__ == '__main__':
    O(Magnets())