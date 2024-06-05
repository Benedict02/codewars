import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def PrependAndAppend():
    n = II()
    s = MSI()
    a = []
    for i in range(len(s)):
        if s[i] == s[-(i+1)]:
            if len(a) >= 2:
                return len(a)
            else:
                return len(s)
        elif s[i] != s[-(i+1)]:
            a = s[i:len(s)-i]
    return len(a)

if __name__ == '__main__':
    for _ in range(II()):
        O(PrependAndAppend())