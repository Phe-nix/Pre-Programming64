"""ภาษาเมืองทิพย์"""
def fact(num, fac):
    """fact"""
    for i in range(1, num+1):
        fac = (fac*i)
    return fac
def main():
    """ภาษาเมืองทิพย์"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    if num1 < num2:
        num2 = num1
    if num3 < num4:
        num4 = num3
    pla = fact(num1, 1)//(fact(num1-num2, 1)*fact(num2, 1))
    pla1 = fact(num3, 1)//(fact(num3-num4, 1)*fact(num4, 1))
    txt = fact(num2+num4, 1)
    if num2 == 0 and num4 == 0:
        print("0 Alphabet")
        print("0 Word")
        return
    elif num2 == 0:
        print("%d Alphabet"%(num4))
        print("%d Word"%(pla1*txt))
        return
    elif num4 == 0:
        print("%d Alphabet"%(num2))
        print("%d Word"%(pla*txt))
        return
    print("%d Alphabet"%(num2+num4))
    print("%d Word"%(pla*pla1*txt))
main()
