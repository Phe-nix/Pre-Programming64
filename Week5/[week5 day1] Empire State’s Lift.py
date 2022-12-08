"""[week5 day1] Empire State Lift"""
def check(k, error, floor_totol, finan_lis, count_floor):
    """docstring"""
    while True:
        k += 1
        if error >= 1:
            break
        if count_floor == floor_totol:
            break
        print("-----")
        print("Lift is going up!")
        if finan_lis[k] == "1":
            count_floor += 1
            print("-----")
            print("Lift has reached the 1st floor!")

        elif finan_lis[k] == "2":
            count_floor += 1
            print("-----")
            print("Lift has reached the 2nd floor!")

        elif finan_lis[k] == "3":
            count_floor += 1
            print("-----")
            print("Lift has reached the 3rd floor!")

        elif finan_lis[k] == "4":
            count_floor += 1
            print("-----")
            print("Lift has reached the 4th floor!")

        elif finan_lis[k] == "5":
            count_floor += 1
            print("-----")
            print("Lift has reached the 5th floor!")

def main():
    """[week5 day1] Empire State Lift"""
    floor = []
    floor_all = ["0", "1", "2", "3", "4", "5"]
    new_lis = []
    finan_lis = []
    dis = -1
    k = -1
    count_floor = 0
    floor_totol = 0
    error = 0
    while True:
        num = input()
        floor.append(num)
        if num == "-":
            floor.remove("-")
            break
    for i in floor_all:
        if i not in floor:
            new_lis.append(i)
    for i in floor_all:
        if i not in new_lis:
            finan_lis.append(i)
    floor_totol = len(finan_lis)
    for i in range(floor_totol+1):
        dis += 1
        if finan_lis[dis] == "0":
            print("Error! Not have this floor.")
            error += 1
            break
        elif IndexError:
            print("OK! Wait please.")
            print("-----")
            print("Lift is arriving!")
            break
    check(k, error, floor_totol, finan_lis, count_floor)
main()
