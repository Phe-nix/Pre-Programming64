"""Kerati, Master of Noodle V.1"""
def main():
    """Kerati, Master of Noodle V.1"""
    mama = input().lower()
    taste = input().lower()
    pork = taste.count("pork")
    num = int(input())
    if mama == "chotipat" and pork >= 1:
        print(280*num)
    elif mama == "chotipat" and pork < 1:
        print(308* num)
    elif mama == "mawai" and pork >= 1:
        print(238*num)
    elif mama == "mawai" and pork < 1:
        print(261*num)
    elif mama == "nisjung" and pork >= 1:
        print((int(280+(((1/8)*280)**(1/2))*3)*num))
    elif mama == "nisjung" and pork < 1:
        print(int((280+(((1/8)*280)**(1/2))*3)*1.1*num))
    elif mama == "yummayro" and pork >= 1:
        print(int(280-((1/16)*(280%100))*num))
    elif mama == "yummayro" and pork < 1:
        print(int(275+((10/100)*275)*num))
    else:
        print("No Data !!")
main()
