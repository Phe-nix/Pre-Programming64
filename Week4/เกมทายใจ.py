"""เกมทายใจ"""
def main():
    """เกมทายใจ"""
    num = int(input())
    num_n = int(input())
    for _ in range(num_n):
        num1 = int(input())
        if num == num1:
            print("Yes! It is %d." %(num))
            break
    if num != num1:
        print("No more chances. You lose.")
main()
