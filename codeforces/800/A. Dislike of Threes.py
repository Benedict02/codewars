import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def DislikeOfThrees():
    s = II()
    lol = []
    for i in range(1, 4000):
        if i % 10 == 3 or i % 3 == 0: continue
        else: lol.append(i)
    return lol[s-1]






if __name__ == '__main__':
    for _ in range(II()):
        O(DislikeOfThrees())