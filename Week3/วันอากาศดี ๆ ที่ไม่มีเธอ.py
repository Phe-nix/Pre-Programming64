"""วันอากาศดี ๆ ที่ไม่มีเธอ"""
def main():
    """วันอากาศดี ๆ ที่ไม่มีเธอ"""
    hum_x = int(input())
    hum_y = int(input())
    cara_x = int(input())
    cara_y = int(input())
    carb_x = int(input())
    carb_y = int(input())
    numa = ((hum_x-cara_x)**2 + (hum_y-cara_y)**2)**0.5
    numb = ((hum_x-carb_x)**2 + (hum_y-carb_y)**2)**0.5
    if numa < numb:
        print("A")
    elif numa > numb:
        print("B")
    elif cara_y > carb_y:
        print("A")
    elif cara_y < carb_y:
        print("B")
    elif cara_x < carb_x:
        print("A")
    elif cara_x > carb_x:
        print("B")
    else:
        print("A")
main()
