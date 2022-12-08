"""Do you know leap year?"""
def main():
    """Do you know leap year?"""
    year = int(input())
    century = (year // 100) * 100
    if year % 4 == 0:
        if century % 400 == 0:
            print("%d is a leap year."%(year))
        else:
            print("%d is not a leap year."%(year))
    else:
        print("%d is not a leap year."%(year))
main()
