"""4 Mista"""
def main():
    """4 Mista"""
    num1 = str(input())
    num2 = num1.lower()
    num4 = num2.count("four")
    num5 = num2.count("4")
    find1 = str(input())
    find2 = find1.lower()
    num3 = len(num1)
    num_count = num2.count(find2)
    if num4 >= 1 or num5 >= 1 or num3%4 == 0 or num_count == 4:
        print("It's not safe four Mista....")
    else:
        print("MISTA, THIS ONE'S 4 U.")
main()
