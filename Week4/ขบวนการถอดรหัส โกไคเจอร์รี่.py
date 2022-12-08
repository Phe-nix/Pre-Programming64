"""ขบวนการถอดรหัส โกไคเจอร์รี่"""
def main():
    """ขบวนการถอดรหัส โกไคเจอร์รี่"""
    num_pass = int(input())
    txt1 = ""
    txt2 = ""
    num = 0
    num1 = 1
    for _ in range(num_pass):
        txt1 += str(input())

    while True:
        txt2 += str(input())
        if txt2[num] == txt1[num]:
            num += 1
            if txt2 == txt1:
                print("Finally, We found this treasure.")
                break
        else:
            txt2 = ""
            num = 0
        num1 += 1
    print(num1)
main()
