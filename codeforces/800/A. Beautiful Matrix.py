import sys

def steps_before_being_beautiful():
    arr = []
    arr.append(list(map(int, sys.stdin.readline().split())))
    arr.append(list(map(int, sys.stdin.readline().split())))
    arr.append(list(map(int, sys.stdin.readline().split())))
    arr.append(list(map(int, sys.stdin.readline().split())))
    arr.append(list(map(int, sys.stdin.readline().split())))
    
    x = [x for x in arr if 1 in x][0]
    where1shouldbe = (2, 2)
    where1 = (arr.index(x), x.index(1))
    if where1shouldbe == where1:
        res = 0
    else:
        res = abs(where1shouldbe[0] - where1[0]) + abs(where1shouldbe[1] - where1[1])
    return res


if __name__ == '__main__':
    sys.stdout.write(str(steps_before_being_beautiful()))