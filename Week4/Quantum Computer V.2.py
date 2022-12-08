"""quantum computer V.2"""
def main():
    """quantum computer V.2"""
    num_qubit = 0
    cout_num = 0
    on_frz = 0
    on_boot = 0
    txt_qcp = ""
    while True:
        txt = input()
        if txt == "FRZ":
            cout_num += 1
            on_frz = 1
        elif txt == "BOOT":
            cout_num += 1
            on_boot = 1
        elif txt == "INC":
            num_qubit = num_qubit + 1
            cout_num += 1
        elif txt == "DEC":
            num_qubit = num_qubit - 1
            cout_num += 1
        elif txt == "DUBL":
            num_qubit = num_qubit * 2
            cout_num += 1
        elif txt == "HALF":
            num_qubit = num_qubit / 2
            cout_num += 1
        elif (on_frz == 0 and on_boot == 1) and cout_num > 1000:
            txt_qcp = ("ERROR: NonAbsoluteZeroLimitExceeded (QCP002)")
            break
        elif (on_frz == 0 and on_boot == 1) and cout_num <= 1000:
            txt_qcp = ("WARN: AbsoluteZero (QCP001)")
            if cout_num >= 1000:
                break
        elif (on_frz == 0 and on_boot == 0) or (on_frz == 1 and on_boot == 0):
            txt_qcp = ("WARN: MissingBootInstruction (QCP003)")
            num_qubit = 0
        if txt == "END":
            break
    if txt_qcp != "":
        print("%s"%txt_qcp)
    print("%.6f"%num_qubit)
main()
