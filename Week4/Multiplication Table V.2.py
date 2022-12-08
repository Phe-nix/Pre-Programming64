"""Multiplication Table V.2"""
def main():
    """Multiplication Table V.2"""
    num1 = 2
    for i in range(num1, 13):
        print("-------------")
        for j in range(1, 13):
            print("%2d x%3d =%4d"%(i, j, i*j))
    print("-------------")
main()
