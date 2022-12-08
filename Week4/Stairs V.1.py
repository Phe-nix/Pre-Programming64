"""Stairs V.1"""
def main():
    """Stairs V.1"""
    num = abs(int(input()))
    num1 = 1
    for i in range(0,num):
        num1 = 1
        for k in range(0, i+1):
            print(num1, end="")
            num1 += 1 
        print("\r")
main()
