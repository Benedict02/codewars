def short():
    n = int(input())
    t = 0
    o = []
    while(n != t):
        x = input()
        if len(x) > 10:
            t+=1
            y = [*x]
            z = y[1:(len(y)-1)]
            o.append((f"{y[0]}{len(z)}{y[len(y)-1]}"))
        else:
            t += 1
            o.append(x)
    for i in range(0, len(o)):
        print(o[i])


if __name__ == '__main__':
    short()