import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def ICPCBaloons():
    n = II()
    s = MSI()
    ex = []
    res = 0
    for i in range(len(s)):
        if s[i] in ex:
            res+=1
        else:
            ex.append(s[i])
            res+=2
    return res

if __name__ == '__main__':
    for _ in range(II()):
        O(ICPCBaloons())