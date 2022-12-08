"""Basic while"""
def main():
    """Basic while"""
    num = 0
    num_sum = []
    while num >= 0:
        num = int(input())
        if num <= -1:
            break
        num_sum.append(num)
    sum_all = sum(num_sum)
    print(sum_all)
main()
