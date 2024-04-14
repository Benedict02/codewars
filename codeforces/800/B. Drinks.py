import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')

def Drinks():
    n = int(I())
    s = list(map(int, I().split()))
    return sum(s)/n

if __name__ == '__main__':
    O(Drinks())