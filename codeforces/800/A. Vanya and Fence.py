import sys

def VanyaNFence():
    n, h = map(int, sys.stdin.readline().split())
    f = list(map(int, sys.stdin.readline().split()))
    res = 0
    for i in range(n):
        if f[i] > h:
            res += 2
        else:
            res += 1
    return res
    
if __name__ == '__main__':
    sys.stdout.write(str(VanyaNFence()))