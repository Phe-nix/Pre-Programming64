"""เอ้า herb herb herb"""
def main():
    """เอ้า herb herb herb"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    num6 = int(input())
    num7 = int(input())
    num8 = int(input())
    num9 = int(input())
    num10 = int(input())
    ans = (num1*(num1 <= 100)) + (num2*(num2 <= 100)) + (num3*(num3 <= 100))\
        + (num4*(num4 <= 100)) + (num5*(num5 <= 100)) + (num6*(num6 <= 100))\
        + (num7*(num7 <= 100)) + (num8*(num8 <= 100)) + (num9*(num9 <= 100))\
        + (num10*(num10 <= 100))
    if ans == 420:
        print("herb")
    else:
        print(ans)
main()
