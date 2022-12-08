"""หมอลำซิ่ง Academia"""
def main():
    """หมอลำซิ่ง Academia"""
    code = input()
    num_1 = 0
    num2 = 0
    for i in code:
        if i == "1":
            num_1 += 1
        if num_1 > num2:
            num2 = num_1
        elif i == "0":
            num_1 = 0
    if num2 <= 1:
        print("Rank D")
    elif num2 == 2:
        print("Rank C")
    elif num2 == 3:
        print("Rank B")
    elif num2 == 4:
        print("Rank A")
    elif num2 == 5:
        print("Rank S")
    elif num2 >= 6:
        print("Rank SSS")
main()
