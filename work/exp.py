n = int(input())
big_1 = 0
list = []
for i in range(n):
    big_2 = int(input())
    list.append(big_2)
    if big_2 > big_1:
        big_1 = big_2
    list.remove(big_1)
    big_1 = 0
a = len(list)
for i in range(1, a + 1, 1):
    big_2 = list[i - 1]
    if big_2 > big_1:
        big_1 = big_2
print(big_1)