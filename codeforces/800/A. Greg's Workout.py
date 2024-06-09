import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def Greg():
    n = II()
    a = MII()
    ch=0;bi=0;ba=0
    for i in range(len(a)):
        if i%3==0:
            ch+=a[i]
        if i%3==1:
            bi+=a[i]
        if i%3==2:
            ba+=a[i]
    res = max(ch,bi,ba)
    if res==ch:
        return "chest"
    if res==bi:
        return "biceps"
    if res==ba:
        return "back"



if __name__ == '__main__':
    O(Greg())