"""[week5 day1] Basic append"""
def main():
    """[week5 day1] Basic append"""
    txt1 = []
    num = int(input())
    for _ in range(num):
        txt = input()
        txt1.append(txt)
    for i in txt1:
        print(i, end=" ")
main()
