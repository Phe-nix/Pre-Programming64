"""OG is waiting for you"""
def main():
    """OG is waiting for you"""
    age = int(input())
    if age < 20:
        perm = input()
    exp = int(input())
    abrd = input()
    if 17 <= age < 20:
        if perm == "Y" and exp >= 12 and abrd == "Y":
            print("You can be in OG!")
        elif perm == "N":
            print("May be next time.")
        else:
            print("May be next time.")
    elif 20 <= age <= 23:
        if exp >= 12 and abrd == "Y":
            print("You can be in OG!")
        else:
            print("May be next time.")
    else:
        print("May be next time.")
main()
