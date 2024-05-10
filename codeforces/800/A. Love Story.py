# https://codeforces.com/problemset/problem/1829/A

# Fly me to the moon!

import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def LoveStory():
    n = int(I())
    a = "codeforces"
    for _ in range(n):
        s = I()
        count = 0
        for i in range(len(a)):
            if a[i] != s[i]:
                count += 1
        O(count)


if __name__ == '__main__':
    LoveStory()