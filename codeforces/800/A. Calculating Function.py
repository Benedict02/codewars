import sys, math

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')

def F():
    n = int(I())
    return math.floor(((-1)**n)*n / 2)

if __name__ == '__main__':
    O(F())