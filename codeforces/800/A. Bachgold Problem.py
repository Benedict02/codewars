import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def BatchgoldProblem():
    n = II()
    s = []
    while n != 0:
        if n % 2 == 0:
            s.append("2")
            n-=2
        else:
            s.append("3")
            n-=3
    s.sort()
    O(len(s))
    O(' '.join(sorted(s)))
    
    # Harun
    # x = n//2
    # s = ["2"]*x
    # if n % 2:
    #     s[-1] = "3"
    # O(x)
    # O(" ".join(s))

if __name__ == '__main__':
    BatchgoldProblem()