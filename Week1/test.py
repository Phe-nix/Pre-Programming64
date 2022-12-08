"""PEP8"""
def main():
    """Week2 day2"""
    txt1 = str(input())
    braed = len(txt1)%10
    burger = txt1.find("burger"and"Burger")
    print("%s%s%s"%(braed*"(|", burger*"{}", braed*"|)"))
main()
