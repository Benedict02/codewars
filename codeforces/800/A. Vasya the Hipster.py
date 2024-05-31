import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def VasyaTheHipster():
    a,b = MII()
    res = min(a,b)
    if a>b:
        return f"{res} {(a-b)//2}"
    elif a==b:
        return f"{res} 0"
    else:
        return f"{res} {(b-a)//2}"



if __name__ == '__main__':
    O(VasyaTheHipster())