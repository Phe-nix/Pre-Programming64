"""กล่อง ใส่ เพชร"""
def main():
    """กล่อง ใส่ เพชร"""
    num = int(input())
    k = 0
    space = -2
    for i in range(1, num+1):
        print(" "*((num-i)*3), end="")
        for j in range(k+1, 0, -1):
            print(j, "", end="")
        print(" "*(space), end="")
        for j in range(1, k+2):
            print(str(j)*(i > 1), "", end="")
        space += 2
        k += 1
        print()
    k = num

    for i in range(1, num+1):
        print(" "*(i*3), end="")
        for j in range(k-1, 0, -1):
            print(j, "", end="")
        print(" "*(num-i-2)+" "*(num-i-2), end="")
        for j in range(1, k):
            print(str(j)*(i < num-1), "", end="")
        space -= 2
        k -= 1
        print()
main()
