# array = input().split(",")
#
# print(len(set(array)))

# array = input().split(",")
#
# k = int(input())
#
# for _ in range(k):
#     array.insert(0, array.pop())
#
# print(*array)

#     2
# 1 2 3 4 5
#     -3

# - [2, 3, 4, 5, 6] = > [12, 15, 16];

array = [2, 2, 4, 5, 6]

# for i in range(-(-len(array)//2)):
#     print(array[i]*array[len(array)-i-1])

array2 = []

for i in array:
    if i not in array2:
        array2.append(i)

print(len(array2))
