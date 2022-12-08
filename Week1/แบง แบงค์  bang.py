"""PEP8"""
def main():
    """Week2 day2"""
    bang = int(input())
    bang_1000 = bang // 1000
    num1 = bang % 1000
    bang_500 = num1 // 500
    num2 = num1 % 500
    bang_100 = num2 // 100
    num3 = num2 % 100
    bang_50 = num3 // 50
    num4 = num3 % 50
    bang_20 = num4 // 20
    print(bang_1000)
    print(bang_500)
    print(bang_100)
    print(bang_50)
    print(bang_20)
main()
