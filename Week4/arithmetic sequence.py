"""arithmetic sequence"""
def main():
    """arithmetic sequence"""
    num_a = int(input())
    num_an = int(input())
    num_d = int(input())
    num_n = ((num_an - num_a)// num_d) + 1
    for i in range(1, num_n+1, 1):
        num_reslut = (num_a + ((i-1)*num_d))
        print(num_reslut)
main()
