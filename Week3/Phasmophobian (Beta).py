"""Phasmophobian (Beta)"""

def main():
    """Phasmophobian (Beta)"""
    txt1 = input()
    txt2 = input()
    if (txt1 != "No Evidence" and txt2 != "No Evidence") and (txt1 != txt2):
        if txt1 == "Spirit box" and txt2 == "Freezing Temperature" or\
        txt1 == "Spirit box" and txt2 == "Freezing Temperature":
            print("I think Wraith is the answer!!!.")
        if txt1 == "EMF Level 5" and txt2 == "Ghost orb" or\
            txt2 == "EMF Level 5" and txt1 == "Ghost orb":
            print("I think Phantom is the answer!!!.")
        if txt1 == "Ghost Writing" and txt2 == "Ghost orb" or\
            txt2 == "Ghost Writing" and txt1 == "Ghost orb":
            print("I think Yurei is the answer!!!.")
        if txt1 == "Freezing Temperature" and txt2 == "EMF Level 5" or\
            txt2 == "Freezing Temperature" and txt1 == "EMF Level 5":
            print("I think Banshee is the answer!!!.")
        if txt1 == "Ghost Writing" and txt2 == "Fingerprints" or\
            txt2 == "Ghost Writing" and txt1 == "Fingerprints":
            print("I think Revenant is the answer!!!.")
        if txt1 == "Spirit box" and txt2 == "Fingerprints" or\
            txt2 == "Spirit box" and txt1 == "Fingerprints":
            print("I think Hantu is the answer!!!.")
    elif txt1 == "No Evidence" and txt2 == "No Evidence":
        print("I think Wraith, Phantom, Yurei, Banshee, Revenant and Hantu, \
            so one of them is the answer!!!.")
    elif (txt1 == "no evidence") or (txt2 == "no evidence") or (txt1 == txt2):
        print("I think Y")
        if txt1 == "Ghost Writing" and txt2 == "No Evidence" or\
           txt2 == "Ghost Writing" and txt1 == "No Evidence":
            print("I think Yurei and Revenant, so one of them is the answer!!!.")
        elif txt1 == "Spirit box" and txt2 == "No Evidence" or\
            txt2 == "Spirit box" and txt1 == "No Evidence":
            print("I think Wraith and Hantu, so one of them is the answer!!!.")
        elif txt1 == "Fingerprints" and txt2 == "No Evidence" or\
            txt2 == "Fingerprints" and txt1 == "No Evidence":
            print("I think Revenant and Hantu, so one of them is the answer!!!.")
        elif txt1 == "Freezing Temperature" and txt2 == "No Evidence" or\
            txt2 == "Freezing Temperature" and txt1 == "No Evidence":
            print("I think Wraith and Banshee, so one of them is the answer!!!.")
        elif txt1 == "EMP Level 5" and txt2 == "No Evidence" or\
            txt2 == "EMP Level 5" and txt1 == "No Evidence":
            print("I think Phantom and Banshee, so one of them is the answer!!!.")
        elif txt1 == "Ghost orb" and txt2 == "No Evidence" or\
            txt2 == "Ghost orb" and txt1 == "No Evidence":
            print("I think Phantom and Yurei, so one of them is the answer!!!.")
main()