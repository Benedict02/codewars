import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def InsomniaCure():
    k = II()
    l = II()
    m = II()
    n = II()
    d = II()

    if k == 1 or l == 1 or m == 1 or n == 1:
        return d
    else:
        r = [0]*d
        for i in range(d):
            if not((i+1)%k) or not((i+1)%l) or not((i+1)%m) or not((i+1)%n):
                r[i] = 1
        return r.count(1)

if __name__ == '__main__':
    O(InsomniaCure())