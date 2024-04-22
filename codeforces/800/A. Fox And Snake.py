import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def FoxNSnake():
    n, m = MI()
    nrml = m * "#"
    rh = (m-1) * "." + "#"
    lh = "#" + (m-1) * "."
    isl = False
    res = []
    for i in range(n):
        if i % 2 == 0:
            res.append(nrml)
        if i % 2 == 1:
            if isl == True:
                res.append(lh)
                isl = False
            else:
                res.append(rh)
                isl = True
    [O(x) for x in res]



if __name__ == '__main__':
    FoxNSnake()