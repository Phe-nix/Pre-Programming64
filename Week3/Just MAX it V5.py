""" Just MAX it V.5"""
def most_of_num(num1, num2):
    """ Just MAX it V.5"""
    if num1 > num2:
        return num1
    else:
        return num2


def main():
    """just MAX"""
    num = float(input())
    ans = most_of_num(num, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    ans = most_of_num(ans, float(input()))
    print("%.2f"%ans)

main()
