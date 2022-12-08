"""Is this a vowel?"""
def main():
    """Is this a vowel?"""
    txt1 = input().upper()
    if (txt1 == "A") or (txt1 == "E") or (txt1 == "I") or (txt1 == "O") or (txt1 == "U"):
        print("%s is vowel."%(txt1))
    else:
        print("%s is consonant."%(txt1))
main()
