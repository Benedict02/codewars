import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def EvenArray():
    n = int(I())
    for _ in range(n):
        ns = int(I())
        a = MI()
        x = []
        for i in range(ns):
            if (a[i] % 2 == 0 and i % 2 == 0) or (a[i] % 2 == 1 and i % 2 == 1):
                continue
            elif a[i]%2 != i%2:
                x.append(a[i])
        genap = []
        ganjil = []
        for i in x:
            if i % 2 == 0:
                genap.append(i)
            else:
                ganjil.append(i)
        if len(x)%2==1:
            O(-1)
        else:
            if len(genap) == len(ganjil):
                O(len(x)//2)
            else:
                O(-1)

if __name__ == '__main__':
    EvenArray()