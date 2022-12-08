"""ตัดกระดาษ"""
def main():
    """ตัดกระดาษ"""
    txt = input()
    num_len = int(input())
    txt_len = len(txt)
    print(txt[0:num_len])
    print(txt[num_len:txt_len])
main()
