"""d"""
dog = "chihuahua,terrier,pug,dog"
pig = "yorkshire,duroc,berkshire,pig"
bread = "banana bread,baguette,breadstick,bread"

prev1 = False
prev2 = False
prev3 = False
prev4 = False
prev5 = False

def y(x):
    global prev1, prev2, prev3, prev4, prev5
    if prev1:
        if prev2:
            if prev3:
                if prev4:
                    if prev5:
                        prev1 = prev2
                        prev2 = prev3
                        prev3 = prev4
                        prev4 = prev5
                        prev5 = x
                    else : prev5 = x
                else : prev4 = x
            else : prev3 = x
        else : prev2 = x
    else: prev1 = x

while True:
    x = input().lower()
    if x == "yorkshire terrier":
        x = "terrier"

    if x == "take care micheal.":
        print("Attack Micheal!!")
        break

    y(x)

    if prev3:
        if ((prev1 in dog) and (prev2 in pig) and (prev3 in bread)):
            print("Error!!!")
            break

    if prev4:
        if ((prev2 in dog) and (prev3 in pig) and (prev4 in bread)):
            print("Error!!!")
            break

    if prev5:
        if ((prev3 in dog) and (prev4 in pig) and (prev5 in bread)):
            print("Error!!!")
            break
    if prev5:
        if prev1 == prev2 and prev2 == prev3 and prev3 == prev4 and prev4 == prev5:
            print("Stand By")
            break
    if prev5:
        if ((prev1 in dog) and (prev2 in dog) and (prev3 in dog) and (prev4 in dog) and (prev5 in dog)):
            print("Stand By")
            break
    if prev5:
        if ((prev1 in pig) and (prev2 in pig) and (prev3 in pig) and (prev4 in pig) and (prev5 in pig)):
            print("Stand By")
            break
    if prev5:
        if ((prev1 in bread) and (prev2 in bread) and (prev3 in bread) and (prev4 in bread) and (prev5 in bread)):
            print("Stand By")
            break
    