def reverse_middle(lst):
    if len(lst) % 2 == 0:
        tup = lst[len(lst)// 2 - 1], lst[len(lst) // 2]
    else:
        tup = lst[len(lst)// 2 - 1], lst[len(lst) // 2], lst[len(lst) // 2 + 1]
    arr = list(tup)
    arr.reverse()
    return arr

if __name__ == '__main__':
    print(reverse_middle([4, 3, 100, 1]))