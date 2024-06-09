import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def DoorsNKeys():
    s = MSI()
    k = []
    for i in range(len(s)):
        if s[i] == 'r':
            k.append('r')
        if s[i] == 'g':
            k.append('g')
        if s[i] == 'b':
            k.append('b')
        if s[i] == 'R':
            if 'r' not in k:
                return "NO"
        if s[i] == 'G':
            if 'g' not in k:
                return "NO"
        if s[i] == 'B':
            if 'b' not in k:
                return "NO"
    return "YES"

if __name__ == '__main__':
    for _ in range(II()):
        O(DoorsNKeys())