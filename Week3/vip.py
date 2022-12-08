"""vip"""
def main():
    """VIP"""
    monney = float(input())
    bool_1 = bool(monney > 0) # Ture
    bool_2 = bool(monney == 0) # False
    print("Welcome!"* bool_1 + "Get out!" * bool_2)
main()
