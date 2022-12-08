""""What grade?"""
def main():
    """"What grade?"""
    grade = int(float(input()))
    if 100 >= grade >= 80:
        print("A")
    elif 75 <= grade <= 79:
        print("B+")
    elif 70 <= grade <= 74:
        print("B")
    elif 65 <= grade <= 69:
        print("C+")
    elif 60 <= grade <= 64:
        print("C")
    elif 55 <= grade <= 59:
        print("D+")
    elif 50 <= grade <= 54:
        print("D")
    elif 0 <= grade < 50:
        print("F")
main()
