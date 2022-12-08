"""ซูม หรือ ซัม V.2"""
def main():
    """ซูม หรือ ซัม V.2"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num1 == num2 == num3:
        print("0")
    elif num1 == num2:
        print(num3)
    elif num2 == num3:
        print(num1)
    elif num1 == num3:
        print(num2)
    elif num1 != num2 or num2 != num3 or num1 != num3:
        print(num1 + num2 + num3)
main()
