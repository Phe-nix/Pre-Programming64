"""d"""
def main():
    mh1 = 0
    ph1 = 0
    sh1 = 0
    wh1 = 0
    gh1 = 0
    y_12 = 0

    while True:
        x = input()
        if x == "END": 
            print(y_12)
            break

        if x == "MH" : mh1 += 1
        elif x == "PH" : ph1 += 1
        elif x == "SH" : sh1 += 1
        elif x == "WH" : wh1 += 1
        elif x == "GH" : gh1 += 1
        else:
            mh1 = 0
            ph1 = 0
            sh1 = 0
            wh1 = 0
            gh1 = 0
            print("ERROR")

        if mh1 >= 1 and ph1 >= 1 and sh1 >= 1 and wh1 >= 1 and gh1 == 1 :
            mh1 = 0
            ph1 = 0
            sh1 = 0
            wh1 = 0
            gh1 = 0
            y_12 += 1
main()
