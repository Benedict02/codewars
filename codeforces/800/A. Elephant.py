import sys
"""
    Skill issue: Learn Dynamic Programming
    Ben does not know Dynamic Programming to solve A. Elephant
    https://www.youtube.com/watch?v=Hdr64lKQ3e4
    I really should prep for TO 2
"""


def Elephant():
    I = int(sys.stdin.readline())
    if I % 5 == 0:
        I /= 5
    elif I % 4 == 0:
        I /= 4
    elif I % 3 == 0:
        I /= 3
    elif I % 2 == 0:
        I /= 2
    elif I % 1 == 0:
        I /= 1
    return int(I)

if __name__ == '__main__':
    sys.stdout.write(str(Elephant()))