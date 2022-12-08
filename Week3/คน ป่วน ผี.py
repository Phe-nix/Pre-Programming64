"""คน ป่วน ผี"""
def main():
    """คน ป่วน ผี"""
    num1 = int(input())
    num_1 = num1//10000
    num_2 = (num1-(num_1*10000))//1000
    num_3 = (num1-(num_1*10000)-(num_2*1000))//100
    num_4 = (num1-(num_1*10000)-(num_2*1000)-(num_3*100))//10
    num_5 = (num1-(num_1*10000)-(num_2*1000)-(num_3*100)-(num_4*10))//1
    num_6 = num_1 + num_2 + num_3 + num_4 + num_5
    num_result = num_6 % 10
    if num_result % 2 == 0 and num_result % 4 == 0:
        print("ผีตานี")
    elif num_result % 2 == 0 and num_result % 4 != 0:
        print("ผีกระหัง")
    elif num_result % 2 != 0 and num_result % 5 == 0:
        print("ผีกระสือ")
    elif num_result % 2 != 0 and num_result % 5 != 0:
        print("ผีปอบ")
main()
