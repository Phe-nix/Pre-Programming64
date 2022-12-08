"""อยากดูพลุ มุแงงงง~"""
def main():
    """อยากดูพลุ มุแงงงง~"""
    num = input()
    length = len(num)
    k = 0
    for i in range(length, k-1):
        for j in range((length+2)*(-1), length+3):
            j = abs(j)
            if i+j == length-1:
                print(num[i+1], end=" ")
            else:
                print(" ", end=" ")
main()


#   6543210123456
#   4     4     4 
#     3   3   3
#       2 2 2

#   4 3 2 1 2 3 4

#       2 2 2
#     3   3   3
#   4     4     4