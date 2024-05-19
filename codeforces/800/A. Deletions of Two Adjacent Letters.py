# I'm guessing
import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def DeletionOfTwoAdjacentLetters():
    t = 1
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        c = input()
        ch = "NO"
        for i in range (n):
            if s[i] == c:
                if i % 2 == 0 and (n - i) % 2:
                    ch = "YES"
                    break
        O(ch)

if __name__ == '__main__':
    DeletionOfTwoAdjacentLetters()