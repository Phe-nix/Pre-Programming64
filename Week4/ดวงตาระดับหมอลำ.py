"""ดวงตาระดับหมอลำ"""
def main():
    """ดวงตาระดับหมอลำ"""
    cup = input()
    time = 0
    while True:
        txt = input()
        if txt == "1":
            if cup == "A":
                cup = "B"
            elif cup == "B":
                cup = "A"
        elif txt == "2":
            if cup == "B":
                cup = "C"
            elif cup == "C":
                cup = "B"
        elif txt == "3":
            if cup == "A":
                cup = "C"
            elif cup == "C":
                cup = "A"
        elif txt == "stop":
            break
        time = time + 1
    print("ball in cup %s"%(cup))
    print("shuffle %d time"%(time))
main()
