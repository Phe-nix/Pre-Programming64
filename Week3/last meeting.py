"""last meeting"""
def main():
    """last meeting"""
    hour = int(input())
    minute = int(input())
    second = int(input())
    time = input().lower()
    minute1 = int(input())
    second1 = int(input())
    second = second1 + second
    second_mn = second % 60
    minute2 = ((minute + minute1) + (second // 60)) % 60
    hour_am = hour + (((minute + minute1) + (second // 60)) // 60)
    hour_pm = hour_am % 12 + (12 * (not hour_am % 12))
    result = ((hour_am // 12) + (hour_am >= 12 and hour == 12))
    if time == "am":
        anw = ("am" * (not result % 2)) + "pm" * (result % 2)
        print("%.2d:%.2d:%.2d %s" % (hour_pm, minute2, second_mn, anw))
    elif time == "pm":
        anw = "am" * (result % 2) + "pm" * (not result % 2)
        print("%02d:%02d:%02d %s" %(hour_pm, minute2, second_mn, anw))
main()
