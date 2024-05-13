import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def wordonthepaper():
    t = int(I())
    for _ in range(t):
        tmp = []
        for _ in range(8):
            tmp.append(I().replace(".", ""))
        O("".join(tmp))

if __name__ == '__main__':
    wordonthepaper()