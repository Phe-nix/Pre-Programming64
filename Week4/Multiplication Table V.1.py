"""Multiplication Table V.1"""
def main():
    """Multiplication Table V.1"""
    num = int(input())
    print("-----------------")
    for i in range(1, 13):
        print("%3d x%4d =%6d" %(num, i, num*i))
    print("-----------------")
main()
