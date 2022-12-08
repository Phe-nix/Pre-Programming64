"""quantum computer V.1"""
def main():
    """quantum computer V.1"""
    num = int(input())
    num_qubit = 0
    i = 0
    for i in range(num):
        qubit = input()
        if qubit == "INC":
            num_qubit = num_qubit + 1
        elif qubit == "DEC":
            num_qubit = num_qubit - 1
        elif qubit == "DUBL":
            num_qubit = num_qubit * 2
        elif qubit == "HALF":
            num_qubit = num_qubit / 2
    print("%.2f"%(num_qubit))
    i = i + 1
main()
