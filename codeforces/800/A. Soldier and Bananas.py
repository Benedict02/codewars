import sys

def SoldierBananas():
    #k = price
    #n = money
    #w = banana
    k, n, w = map(int, sys.stdin.readline().split())
    for i in range(1, w+1):
        n -= i * k
    if n < 0:
        return abs(n)
    else:
        return 0

if __name__ == '__main__':
    sys.stdout.write(str(SoldierBananas()))