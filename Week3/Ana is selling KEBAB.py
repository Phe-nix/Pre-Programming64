"""Ana is selling KEBAB"""
def main():
    """Ana is selling KEBAB"""
    pice = int(input())
    num1 = int(input())
    pice_kebub = pice * num1
    txt1 = input()
    if txt1 == "This kebab is very good":
        promotion = pice_kebub * (70/100)
        print("%.2f"%(promotion))
    elif txt1 == "This is not good not bad":
        promotion = pice_kebub * (95/100)
        print("%.2f"%(promotion))
    elif txt1 == "This is not kebab":
        promotion = pice_kebub * (16/100)+pice_kebub
        print("%.2f"%(promotion))
    else:
        print("0.00")
main()
