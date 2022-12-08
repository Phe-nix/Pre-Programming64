"""[quiz] Strong Password"""
def main():
    """[quiz] Strong Password"""
    password = input()
    score = 0
    alpha = 0
    num = 0
    upper = 0
    lower = 0
    same = -1
    if len(password) < 6:
        print("try again")
        password = input()
    elif len(password) >= 6:
        if len(password) >= 6:
            for i in range(len(password)):
                if password[i].isnumeric():
                    num += 1
                elif password[i].isalpha():
                    alpha += 1
                elif password[i].islower():
                    lower += 1
                elif password[i].isupper():
                    upper += 1
                elif password[0] == password[i]:
                    same += 1
            de_same = same - 3
            if password.isnumeric():
                score += 50
            elif password.isalpha():
                score += 30
            elif password.islower():
                score += 100
            elif password.isupper():
                score += 85
            elif num >= 1 and alpha >= 1:
                score += 75
            elif lower >= 1 and upper >= 1:
                score += 175
            elif same > 3:
                score -= de_same*15
            elif len(password) > 10:
                password_len = abs(10 - len(password))
                score += password_len * 15
            score = score + ord(password[(len(password))-1])
            if score < 150:
                score_re = ("poor")
            elif score < 300:
                score_re = ("acceptable")
            elif score >= 300:
                score_re = ("secure")
            print("Password : %s"%((len(password))*"*"))
            print("Security score : %d"%(score))
            print("Security level : %s"%(score_re))
    elif len(password) < 6:
        print("process terminated") 
main()
