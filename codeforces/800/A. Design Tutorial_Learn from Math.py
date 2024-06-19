import sys, math

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def isPrime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def DesignTutorial_LearnFromMath(n):
    if n%2 == 0:
        t1 = n//2
        t2 = n//2
        while t1 % 2 or t2 % 2:
            t1 += 1
            t2 -= 1
    else:
        t1 = n//2
        t2 = n//2 + 1
        while isPrime(t1) or isPrime(t2):
            t1 += 1
            t2 -= 1
    # fstring slow, join fast
    # return f"{t1} {t2}"
    return " ".join(map(str, [t1, t2]))
    
if __name__ == '__main__':
    n = II()
    O(DesignTutorial_LearnFromMath(n))