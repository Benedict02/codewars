import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')

def George():
    n = int(I())
    r = 0
    while n:
        n -= 1
        s = list(map(int, I().split()))
        if s[1] - s[0] >= 2:
            r += 1
    return r

if __name__ == '__main__':
    O(George())