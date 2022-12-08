"""What is it then?"""
def main():
    """What is it then?"""
    txt1 = input()
    if txt1.isalpha() == True:
        print("'%s' is an alphabet."%(txt1))
    elif txt1.isnumeric() == True:
        print("'%s' is numeric."%(txt1))
    else:
        print("'%s' is not both an alphabet and numeric."%(txt1))
main()
