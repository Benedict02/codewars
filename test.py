n = int(input())

#     *
#    **
#   ***
#  ****
# *****

for i in range(1, n):
    for j in range(n-i, 1, -1):
        print(""*j, end=" ")
    print("*"*i)


# n = int(input())
# [([print(""*j, end=" ") for j in range(n-i, 1, -1)], print("*"*i)) for i in range(1, n)]
