"""[week5 day1] Basic split"""
def main():
    """[week5 day1] Basic split"""
    txt = input()
    txt_s = input()
    print(txt.split(txt_s))
    for i in txt.split(txt_s):
        print(i)
main()
