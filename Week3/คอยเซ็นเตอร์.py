"""คอยเซ็นเตอร์"""
def main():
    """คอยเซ็นเตอร์"""
    money = int(input())
    num_min = int(input())
    num_sec = int(input())
    if money == 0:
        print("free")
    elif num_sec <= 30:
        if num_min <= 2:
            print("free")
        elif num_min <= 15:
            print(money*15)
        elif num_min > 15:
            print(money*num_min)
    elif num_sec > 30:
        if num_min+1 <= 2:
            print("free")
        elif num_min+1 <= 15:
            print(money*15)
        elif num_min+1 > 15:
            print(money*(num_min+1))
main()
