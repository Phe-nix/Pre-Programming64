"""นักแปลงข้อมูล"""
def main():
    """นักแปลงข้อมูล"""
    txt = input()
    txt1 = ""
    for i in txt:
        if i == "z":
            txt_a = "e"
        elif i.isalpha():
            txt_a = ord(i)
            txt_a = chr(txt_a + 5)
            txt_a = txt_a.replace("[", "A")
            txt_a = txt_a.replace("\\", "B")
            txt_a = txt_a.replace("]", "C")
            txt_a = txt_a.replace("^", "D")
            txt_a = txt_a.replace("_", "E")
            txt_a = txt_a.replace("{", "a")
            txt_a = txt_a.replace("|", "b")
            txt_a = txt_a.replace("}", "c")
            txt_a = txt_a.replace("~", "d")
            txt_a = txt_a.replace(">", "4")
        elif i.isnumeric():
            txt_a = ord(i)
            txt_a = chr(txt_a + 5)
            txt_a = txt_a.replace(":", "0")
            txt_a = txt_a.replace(";", "1")
            txt_a = txt_a.replace("<", "2")
            txt_a = txt_a.replace("=", "3")
            txt_a = txt_a.replace(">", "4")
        else:
            txt_a = i
        txt1 += txt_a


    print(txt1)
main()
