"""Apex pack"""
def main():
    """Apex pack"""
    level = int(input())
    lv1 = level-1
    lv21 = 19+((level-20)//2)
    lv301 = 159+((level-300)//5)
    if 1 <= level <= 20:
        print("%d"%(lv1) + " Packs opened")
        print("%d"%(500-lv1) + " Packs more")
    elif 21 <= level <= 300:
        print("%d"%(lv21) + " Packs opened")
        print("%d"%(500-lv21) + " Packs more")
    elif 301 <= level <= 500:
        print("%d"%(lv301) + " Packs opened")
        print("%d"%(500-lv301) + " Packs more")
    elif level > 500:
        print("199 Packs opened")
        print("301 Packs more")
main()
