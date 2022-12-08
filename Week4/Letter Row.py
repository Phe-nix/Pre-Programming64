"""Letter Row"""
def main():
    """Letter Row"""
    num = int(input())
    txt2 = ""
    for _ in range(num):
        txt = input()
        for j in txt:
            if j.isalpha():
                txt2 += j
    print(txt2)
main()
