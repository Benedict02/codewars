import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def RestoringThreeNumbers(x1, x2, x3, x4):
    arr = [x1, x2, x3, x4]
    arr.sort()
    a = (arr[0]-arr[1]+arr[2])//2
    b = (arr[0]-arr[2]+arr[1])//2
    c = arr[-1] - a - b
    return " ".join(map(str, [a, b, c]))

if __name__ == "__main__":
    x1, x2, x3, x4 = MII() 
    O(RestoringThreeNumbers(x1, x2, x3, x4))