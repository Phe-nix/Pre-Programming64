"""Car Park"""
def main():
    """Car Park"""
    day_in = int(input())
    time_in = int(input())
    day_out = int(input())
    time_out = int(input())
    time = time_out - time_in 
    pay = 0
    dis = 0
    if day_in > day_out or time_out >= 24 or time_in >= 24 or day_in <= 0 or day_in > 365 or\
    day_out <= 0 or day_out > 365:
        print("error")
    else:
        if day_in - day_out == 0:
            if time_in > time_out:
                print("error")
            elif time_out == time_in:
                print("0 day 0 hour")
                print("0 baht")
            else:
                print("0 day %d hour"%(time))
                print("%d baht"%(pay))
        else:
            if time_in == time_out:
                daycar = day_out - day_in
                time = 0
            elif time_in-time_out >= 0:
                daycar = day_out-day_in-1
                day = time//24
                time = time-(day*24)
            elif time_in-time_out < 0:
                daycar = day_out-day_in
                day = time//24
                time = time - (day*24)
            pay = pay + daycar * 200 + (time * 15 *(2 < time <= 12)) + 200 * (time > 12)
            dis = (daycar//7)*300
            dis = dis + 500 * (daycar >= 28)
            print("%d day %d hour" % (daycar, time)) 
            print("%d baht"%(pay - dis))
main()
++++++