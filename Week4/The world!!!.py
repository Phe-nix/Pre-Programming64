"""The world!!!"""
def main():
    """The world!!!"""
    void_x = int(input())
    void_y = int(input())
    num_n = int(input())
    chono = 0
    for _ in range(num_n):
        num_x = int(input())
        num_y = int(input())
        distance = (((num_x-void_x)**2) + ((num_y-void_y)**2))**0.5
        if distance <= 500:
            chono = chono + 1
    if chono == 1:
        print("You got 1 enemy in your area.")
    elif chono > 1:
        print("You got %d enemies in your area."%chono)
    elif chono == 0:
        print("Muda Muda Muda.")
main()
