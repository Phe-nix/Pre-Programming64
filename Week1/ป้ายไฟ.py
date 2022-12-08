"""ป้ายไฟ"""
def main():
    """ป้ายไฟ"""
    txt1 = input().upper()
    txt_len = str(txt1)
    txt2 = len(txt_len)
    txt3 = int(txt2 + 4)
    print("|%s|"%(txt3*"-"))
    print("|  %s  |"%(txt1))
    print("|%s|"%(txt3*"-"))
main()
