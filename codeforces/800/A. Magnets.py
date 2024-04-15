import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')

def Magnets():
    n = int(I())
    s = []
    res = 1
    for i in range(n):
        s.append(I())
        if len(s) > 1:
            if s[i] != s[i-1]:
                res += 1
    return res


if __name__ == '__main__':
    O(Magnets())