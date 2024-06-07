import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def SerejaAndDima():
    n = II()
    a = MII()
    d = 0; s = 0
    if len(a)>1:
        for i in range(n):
            val = max(a[0], a[-1])
            if val == a[0]:
                val = a.pop(0)
            else:
                val = a.pop(-1)
            if i%2:
                d+=val
            else:
                s+=val
        return str(s)+" "+str(d)


    elif len(a) == 1:
        return str(a[0]) + " 0"

if __name__ == '__main__':
    O(SerejaAndDima())