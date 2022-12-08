"""[quiz] Xbox"""
def main():
    """[quiz] Xbox"""
    num = int(input())
    for i in range(num):
        for j in range(num):
            output = ' '
            if i == 0:
                output = "*"
            elif  j == num-1:
                output = "*"
            elif i > 0 and j == 0:
                output = "*"
            elif i == num-1 and 0 <= j < num:
                output = "*"
            elif i == j or i+j == num-1:
                output = "*"
            print(output, end=" ")
        print()
main()
