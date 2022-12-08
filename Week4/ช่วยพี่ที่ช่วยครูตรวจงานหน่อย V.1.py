"""ช่วยพี่ที่ช่วยครูตรวจงานหน่อย V.1"""
def main():
    """ช่วยพี่ที่ช่วยครูตรวจงานหน่อย V.1"""
    txt1 = input()
    txt2 = input()
    txt4 = txt1.lower()
    txt5 = txt2.lower()
    txt3 = ""
    score = 10
    score_10 = 0
    txt1_num = len(txt1)
    for i in range(txt1_num):
        if txt5[i] == txt4[i]:
            txt3 += txt2[i]
        elif txt5[i] != txt4[i]:
            txt3 += ("(%s)"%txt2[i])
            score -= 1
    if score == -score:
        score_10 = 0
    elif 10 >= score >= 1:
        score_10 = score
    print(txt3)
    print("%d/10 (-%d)"%(score_10, 10-score))
main()
