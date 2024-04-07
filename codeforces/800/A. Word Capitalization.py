import sys

def WordCapitalize():
    I = list(sys.stdin.readline())
    I[0] = I[0].upper()
    return "".join(I)

if __name__ == '__main__':
    sys.stdout.write(str(WordCapitalize()))