import sys

def nextRound():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    if k == n and a[k - 1] != 0: return n
    for i in range(k, n):
        if a[i] >= a[k - 1]:
            k = i + 1
        else:
            break
    return k if a[k - 1] != 0 else k - a.count(0)

if __name__ == '__main__':
    sys.stdout.write(str(nextRound()))