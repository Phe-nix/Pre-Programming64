"""[week5 day1] Basic index"""
def main():
    """[week5 day1] Basic index"""
    txt1 = []
    while True:
        txt = input()
        txt1.append(txt)
        if txt.upper() == "END":
            position = int(input())
            break
    position_len = len(txt1)
    if position > position_len-1:
        print("Index Not Found")
    else:
        print("List[%d] = \"%s\" "%(position, txt1[position]))
main()
