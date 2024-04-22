import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def Iloveusername():
    n = int(I())
    s = MI()
    res = 0
    if len(s) > 1:
        low = min(s[0], s[1])
        high = max(s[0], s[1])
        if s[0] < s[1]:
            res += 1
        if s[0] > s[1]:
            res += 1
    for i in range(n):
        if i < n-1:
            if s[i] < s[i+1] and s[i+1] > high:
                res += 1
                high = max(high, s[i+1])
            if s[i] > s[i+1] and s[i+1] < low:
                res += 1
                low = min(low, s[i+1])
    return res


if __name__ == '__main__':
    O(Iloveusername())