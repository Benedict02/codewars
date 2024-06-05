import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def PrependAndAppend():
    n = II()
    s = MSI()
    res = n
    # .join is O(n), list() is O(n) so my algorithm is O(n^2) which is not good for python
    # for i in range(len(s)):
    #     if s[i] == s[-(i+1)]:
    #         if len(a) >= 2:
    #             return len(a)
    #         else:
    #             return len(s)
    #     elif s[i] != s[-(i+1)]:
    #         a = s[i:len(s)-i]
    # return len(a)
    # I need to use pointers:
    while res>1:
        p1 = s.pop(0)
        p2 = s.pop(-1)
        if p1==p2:
            break
        res-=2
    return res
    

if __name__ == '__main__':
    for _ in range(II()):
        O(PrependAndAppend())