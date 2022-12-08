"""[quiz] Kira's Number"""
def main():
    """[quiz] Kira's Number"""
    num = input()
    mylist = []
    reslut_new = ""
    reslut_len_new = 0
    for i in range(len(num)):
        mylist.append(int(num[i]))
    reslut = sum(mylist)
    reslut = reslut**3
    reslut_new = str(reslut + int(num[0:5]))
    reslut_len = len(str(reslut))
    if reslut_len < 5:
        reslut_len_new = 5 - reslut_len 
    print("%s%s"%(reslut_len_new*"0",reslut_new[0:5]))
main()
