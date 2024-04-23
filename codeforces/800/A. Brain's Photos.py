import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def BrainPhotos():
    n, m = MI()
    temp = []
    res = 0
    for i in range(n):
        temp.append(I().split())
    for i in range(len(temp)):
        if "C" in temp[i] or "M" in temp[i] or "Y" in temp[i]:
            res += 1
        else:
            res -= 0
        
    return "#Color" if res > 0 else "#Black&White"




if __name__ == '__main__':
    O(BrainPhotos())