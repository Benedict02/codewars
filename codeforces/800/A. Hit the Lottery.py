import sys,math

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))



def HitTheLottery():
    n = II()
    res = 0

    # if math.log10(n).is_integer() and n > 1:
    #     return n//100

    while n > 0:
        if n >= 100:
            res += n//100
            n = n % 100
        elif n >= 20:
            res += n//20
            n = n % 20
        elif n >= 10:
            res += n//10
            n = n % 10
        elif n >= 5:
            res += n//5
            n = n % 5
        elif n >= 1:
            res += n//1
            n = n % 1
    
    return res


if __name__ == '__main__':
    O(HitTheLottery())