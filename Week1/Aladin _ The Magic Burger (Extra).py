"""PEP8"""
def main():
    """Week2 day2"""
    txt1 = str(input())
    bread = len(txt1)%10
    txt2 = txt1.lower()
    burger = txt2.find("burger")
    print("%s%s%s"%(bread*"(|", burger*"{}", bread*"|)"))
main()
