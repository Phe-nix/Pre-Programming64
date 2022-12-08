""" Way to travel"""
def main():
    """ Way to travel"""
    weather = input()
    impt = input()
    distance = float(input())
    if distance < 0:
        print("Error")
    elif weather == "sunny":
        if 0 <= distance < 1:
            print("Walk")
        elif 1 <= distance < 20:
            print("Motorcycle")
        elif 20 <= distance < 300:
            print("Car")
        elif distance >= 300:
            print("Private jet")
    elif weather == "rainy" and impt == "important":
        if 0 <= distance < 1:
            print("Walk")
        elif 1 <= distance < 20:
            print("Motorcycle")
        elif 20 <= distance < 300:
            print("Car")
        elif distance >= 300:
            print("Private jet")
    elif weather == "rainy" and impt == "not important":
        print("Not go")
main()
