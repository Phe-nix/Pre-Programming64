"""Final Battle"""
def main():
    """Final Battle"""
    power_ben = int(input())
    power_gwen = int(input())
    power_gwen_per = int(input())
    power_sui_gogo = int(input())
    power_new_gwen = power_gwen * (power_gwen_per / 100)
    if power_new_gwen + power_sui_gogo > power_ben:
        print("The world is save!")
    elif power_new_gwen + power_sui_gogo == power_ben:
        print("The world is save but we lost our hero.")
    elif power_new_gwen + power_sui_gogo < power_ben:
        print("Ben 99 is going to ruin the world.")
main()
