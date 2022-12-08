"""วิถีหมอลำ"""
def main():
    """วิถีหมอลำ"""
    num_all = int(input())
    score_sum = 0
    score = 0
    score_list = []
    for _ in range(num_all):
        num1 = int(input())
        num2 = int(input())

        if num1 == num2:
            score = score + 1
            score_list.append(score)
        elif num1 != num2:
            score = 0
            score_list.append(-1)
    score_sum = sum(score_list)
    print("%d Point"%(score_sum))
main()
