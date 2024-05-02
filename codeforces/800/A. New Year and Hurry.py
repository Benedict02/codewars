import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def NewYearNHurry():
    # 20:00 - 00:00
    # needs to be <= 4 hours(240 minutes)
    # n = number of problems
    # k = minutes needed to go home
    n, k = MI()
    res = 0
    for i in range(1, n+1):
        if (5 * i) + k <= 240:
            k += (5*i)
            res += 1
    return res

if __name__ == '__main__':
    O(NewYearNHurry())