"""Kanomwhan Bakery"""
def main():
    """Kanomwhan Bakery"""
    people = int(input())
    price = float(input())
    disc = int(input())
    ans1 = (people*price)-((disc/100)*(people*price))
    ans2 = (((people//4)*3)+(people%4))*price
    if people < 3:
        print("Promotion 1 " + "%0.03f" %(people*price) + " Baht")
        print("Purchase successfully !")
        print("Have a good meal with \"Kanomwhan\"")
    elif ans1 <= ans2:
        print("Promotion 1 " + "%.03f" %(ans1) + " Baht")
        print("Purchase successfully !")
        print("Have a good meal with \"Kanomwhan\"")
    elif ans1 > ans2:
        print("Promotion 2 " + "%.03f" %(ans2) + " Baht")
        print("Purchase successfully !")
        print("Have a good meal with \"Kanomwhan\"")
main()
