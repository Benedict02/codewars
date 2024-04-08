import sys

def changeWord():
    I = list(sys.stdin.readline())
    I.pop()
    I = "".join(I)
    no = 0
    cp = 0
    for i in range(len(I)):
        if ord(I[i]) < 97:
            cp += 1
        else:
            no += 1
    if cp > no:
        return I.upper()
    else:
        return I.lower()

if __name__ == '__main__':
    sys.stdout.write(str(changeWord()))