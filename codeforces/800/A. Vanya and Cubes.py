import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def VanyaNCubes():
    cubes = int(I())
    tot = 0
    everyheightpercube = 0
    level = 1
    res = 0
    while(tot + everyheightpercube + level <= cubes):
        everyheightpercube += level
        level += 1
        res += 1
        tot += everyheightpercube
    return res

if __name__ == '__main__':
    O(VanyaNCubes())