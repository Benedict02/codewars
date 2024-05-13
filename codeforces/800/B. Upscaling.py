import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def Upscaling():
    t = int(I())
    h = True
    for _ in range(t):
        n = int(I())
        
        #   ##..##\n c = 1
        #   ##..##\n c = 2
        #   ..##..\n c = 1
        #   ..##..\n c = 2
        #   ##..##\n c = 1
        #   ##..##\n c = 2
        
        res = []
        for i in range(n):
            if i % 2 == 0:
                for j in range(2):
                    for k in range(n):
                        if k % 2 == 0:
                            res.append("#"*2)
                        else:
                            res.append("."*2)
                    res.append("\n")
            else:
                for j in range(2):
                    for k in range(n):
                        if k % 2 == 0:
                            res.append("."*2)
                        else:
                            res.append("#"*2)
                    res.append("\n")


        O("".join(res), sep="")







if __name__ == '__main__':
    Upscaling()