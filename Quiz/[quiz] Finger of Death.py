"""[quiz] Finger of Death"""
def main():
    """[quiz] Finger of Death"""
    lv_lion = int(input())
    kill_lion = int(input())
    inve = 0
    limit = 0
    damaged = 0
    item_slot = []
    Kaya_and_Sange = 0
    Yasha_and_Kaya = 0
    Sange_and_Yasha = 0
    while True:
        item = input().lower
        inve += 1
        limit += 1
        item_slot.append(item)
        if item == "no more item":
            break
        elif inve == 9:
            break
        
main()