""" Lucky One V.1"""
def main():
    """ Lucky One V.1"""
    txt1 = input().lower()
    txt_num = int(input())
    txt2 = txt1.replace(" ", "")
    print(txt2[txt_num-1])
main()
