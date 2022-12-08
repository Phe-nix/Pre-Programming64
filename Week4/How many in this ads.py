"""How many in this ads?"""
def main():
    """How many in this ads?"""
    txt_num = 0
    txt_up = 0
    txt_low = 0
    txt = input()
    for i in txt:
        if i.isnumeric() == True:
            txt_num = txt_num + 1
        elif i.isalpha() == True:
            if i.islower() == True:
                txt_low = txt_low + 1
            elif i.isupper() == True:
                txt_up = txt_up + 1
    print("%d number(s)"%txt_num)
    print("%d uppercase letter(s)"%txt_up)
    print("%d lowercase letter(s)"%txt_low)
main()
