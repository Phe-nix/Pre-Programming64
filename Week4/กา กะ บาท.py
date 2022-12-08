"""กา กะ บาท"""
def main():
    """กา กะ บาท"""
    num = input()
    length = len(num)
    for i in range(length):
        for j in range(length):
            if i == j or i+j == length-1:
                print(num[j], end=" ")
            else:
                print(" ", end=" ")
        print()
main()
#              i
#   0123456      j
#   1     4    0
#     2 3      1
#     2 3      2
#   1     4    3
#
#              i
#   01234        j
#   1   3      0
#     2        1
#   1   3      2
