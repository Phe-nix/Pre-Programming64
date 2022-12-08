"""Lucky One V.2"""
def main():
    ''''Lucky One V.2'''
    txt1 = input().upper()
    txt2 = txt1.replace(" ", "")
    txt3 = len(txt2)
    print(txt2[txt3-1])
main()
