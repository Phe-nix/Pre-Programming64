"""burger"""
def main():
    """burger"""
    buntop = False
    bunbottom = False
    exotic = False

    while True:
        x12 = input()

        if x12 == "End":

            if exotic or not buntop or not bunbottom:
                print("I'm not sure if it is a Windy Burger.")
            else:
                print("This is your burger, have a good meal.")
            break

        if x12 == "Vegetables":
            print("We have to cancel your order! Get out!!")
            break

        if x12 == "Bun":
            if buntop == False:
                buntop = True
            elif bunbottom == False:
                bunbottom = True
        elif (x12 == "Cheese") or (x12 == "Egg") or (x12 == "Ketchup") or (x12 == "Mayonnaise") or\
             (x12 == "Beef steak") or (x12 == "Chicken steak") or (x12 == "Fish steak") or\
             (x12 == "Bacon") or (x12 == "Sausage") or (x12 == "French fries"):
            if not buntop:
                exotic = True
            bunbottom = False
        else:
            exotic = True
main()
