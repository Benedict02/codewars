import sys,math

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(sys.stdin.readline().replace('\n', ''))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def YetAnother2IntProblem(a, b):
    st = 0
    # while a != b:
    #     if a == b:
    #         return st
    #     elif a > b:
    #         if a == b:
    #             return st
    #         elif a - 1 == b:
    #             a-=1
    #             st+=1
    #         elif a - 2 == b:
    #             a-=2
    #             st+=1
    #         elif a - 3 == b:
    #             a-=3
    #             st+=1
    #         elif a - 4 == b:
    #             a-=4
    #             st+=1
    #         elif a - 5 == b:
    #             a-=5
    #             st+=1
    #         elif a - 6 == b:
    #             a-=6
    #             st+=1
    #         elif a - 7 == b:
    #             a-=7
    #             st+=1
    #         elif a - 8 == b:
    #             a-=8
    #             st+=1
    #         elif a - 9 == b:
    #             a-=9
    #             st+=1
    #         else:
    #             a-=10
    #             st+=1
    #     elif a < b:
    #         if a == b:
    #             return st
    #         elif a + 1 == b:
    #             a+=1
    #             st+=1
    #         elif a + 2 == b:
    #             a+=2
    #             st+=1
    #         elif a + 3 == b:
    #             a+=3
    #             st+=1
    #         elif a + 4 == b:
    #             a+=4
    #             st+=1
    #         elif a + 5 == b:
    #             a+=5
    #             st+=1
    #         elif a + 6 == b:
    #             a+=6
    #             st+=1
    #         elif a + 7 == b:
    #             a+=7
    #             st+=1
    #         elif a + 8 == b:
    #             a+=8
    #             st+=1
    #         elif a + 9 == b:
    #             a+=9
    #             st+=1
    #         else:
    #             a+=10
    #             st+=1
    # return st
    if abs(a-b) % 10 > 0:
        return (abs((a-b))//10)+1
    else:
        return abs(a-b)//10

if __name__ == '__main__':
    for _ in range(II()):
        a, b = MII()
        O(YetAnother2IntProblem(a,b))