"""How many digit?"""
def main():
    """How many digit?"""
    num_1 = input()
    num1 = num_1.count("1")
    num2 = num_1.count("2")
    num0 = num_1.count("0")
    num3 = num_1.count("3")
    num4 = num_1.count("4")
    num5 = num_1.count("5")
    num6 = num_1.count("6")
    num7 = num_1.count("7")
    num8 = num_1.count("8")
    num9 = num_1.count("9")
    print(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num0)
main()
