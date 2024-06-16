import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def BuyAShovel(k, r):
    res = 1
    cost = k
    while True:
        if cost % 10 == 0 or cost % 10 == r:
            return res
        else:
            cost += k
            res += 1

if __name__ == '__main__':
    k,r = MII()
    O(BuyAShovel(k, r))