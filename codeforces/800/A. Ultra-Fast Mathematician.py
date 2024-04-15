import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')

def QuickMaths():
    n1 = [*I()]
    n2 = [*I()]
    n1 = list(map(int, n1))
    n2 = list(map(int, n2))
    res = []
    for i in range(len(n1)):
        if(n1[i] == n2[i]):
            res.append(0)
        else:
            res.append(1)
    return "".join(list(map(str, res)))

if __name__ == '__main__':
    O(QuickMaths())