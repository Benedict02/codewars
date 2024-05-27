import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def HolidayOfEquality():
    n = II()
    k = -1
    c = [0]*n
    res = 0
    a = MII()
    for i in range(n):
        if a[i] > k:
            k = a[i]
    for j in range(n):
        if a[j] != k:
            c[j] = (k-a[j])
            res += c[j]
    return res



if __name__ == '__main__':
    O(HolidayOfEquality())