"""Stairs V.1"""
def main():
    """Stairs V.1"""

    num = abs(int(input()))
    txt = ""
    txt1 = ""
    for i in range(1, num+1, 1):
        txt += str(i)
        txt1 = str(i-1)*(i-1 != 0)+txt1
        print(txt+txt1)

main()
