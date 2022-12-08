"""Orange Cake"""
def main():
    """"Orange Cake"""
    money = int(input())
    pice_cake = int(input())
    number_cake = money // pice_cake
    moist_cake = number_cake * pice_cake
    money_back = money - moist_cake
    if money >= pice_cake:
        print("Orange Cake: %d"%(number_cake))
        print("Money left: %d"%(money_back))
    else:
        print("Not enough money;(")
        print("Money left: %d"%(money))
main()
