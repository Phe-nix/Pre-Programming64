"""Alphabet Order V.2"""
def main():
    """Alphabet Order V.2"""
    num1 = int(input())
    num2 = num1 + 64
    num3 = chr(num2)
    num_lower = num3.lower()
    num_upper = num3.upper()
    print("%s, %s"%(num_lower, num_upper))
main()
