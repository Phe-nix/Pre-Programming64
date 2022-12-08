"""d"""
def main():
    """d"""
    sumtext = ""
    while True:
        txt = input().lower()
        if txt == "end":
            txt2 = input().lower()
            if txt2.isalpha() == False:
                print(0)
                break
            print(sumtext.count(txt2))
            break
        sumtext += txt.lower() + " "
main()
