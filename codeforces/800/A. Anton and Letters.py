import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def AntonNLetters():
    s = I().replace('{', '').replace('}', '').replace(',', '')
    arr = s.split()
    return len(set(arr))

if __name__ == '__main__':
    O(AntonNLetters())